package cmd

import (
	"bytes"
	"fmt"
	"log"
	"os"
	"time"

	"github.com/spf13/cobra"

	//"golang.design/x/clipboard"
	"github.com/atotto/clipboard"
	//"github.com/Duckduckgot/gtts"

	//htgotts "github.com/hegedustibor/htgo-tts"
	//handlers "github.com/hegedustibor/htgo-tts/handlers"
	//voices "github.com/hegedustibor/htgo-tts/voices"

	"github.com/amitybell/piper" // Import the piper package for text-to-speech
	// jenny "github.com/amitybell/piper-voice-jenny" // Jenny's voice is available but not used in this example
	alan "github.com/amitybell/piper-voice-alan" // Import Alan's voice from the piper package

	"github.com/gopxl/beep"         // Import the beep package for playing audio
	"github.com/gopxl/beep/speaker" // Import the speaker package to output the audio
	"github.com/gopxl/beep/wav"     // Import the wav package to decode the wav audio
)

func prepare(tts *piper.TTS, content string) (*beep.StreamSeekCloser, *beep.Format, error) {
	wavBytes, err := tts.Synthesize(content)
	if err != nil {
		return nil, nil, err
	}

	r := bytes.NewReader(wavBytes)

	streamer, format, err := wav.Decode(r)
	if err != nil {
		return &streamer, &format, err
	}

	return &streamer, &format, nil
}

func play(streamer *beep.StreamSeekCloser, done chan bool) {
	speaker.Play(beep.Seq(*streamer, beep.Callback(func() {
		done <- true
	})))
}

func read(content string) {
	tts, err := piper.New("", alan.Asset)
	if err != nil {
		log.Fatal(err)
	}

	midpoint := len(content) / 2
	firstHalf := content[:midpoint]
	secondHalf := content[midpoint:]

	streamer, format, err := prepare(tts, firstHalf)
	if err != nil {
		log.Fatal(err)
	}
	speaker.Init(format.SampleRate, format.SampleRate.N(time.Second/10))
	done := make(chan bool)
	play(streamer, done)
	streamer, format, err = prepare(tts, secondHalf)
	if err != nil {
		log.Fatal(err)
	}
	<-done
	speaker.Init(format.SampleRate, format.SampleRate.N(time.Second/10))
	done = make(chan bool)
	play(streamer, done)
	<-done
}

var rootCmd = &cobra.Command{
	Use:   "hugo",
	Short: "Hugo is a very fast static site generator",
	Long: `A Fast and Flexible Static Site Generator built with
                love by spf13 and friends in Go.
                Complete documentation is available at http://hugo.spf13.com`,
	Run: func(cmd *cobra.Command, args []string) {
		log.Println("hugo func")
		content, err := clipboard.ReadAll()
		if err != nil {
			log.Println("Error reading clipboard:", err)
			return
		}
		log.Println(content)
		read(content)
	},
}

func Execute() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
