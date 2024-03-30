package cmd

import (
	"os"
	"log"
	"fmt"
	"bytes"
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
		//speech := htgotts.Speech{Folder: "audio", Language: voices.English, Handler: &handlers.MPlayer{}}
		//speech.Speak(content)
			// Initialize a new piper instance with Alan's voice
		tts, err := piper.New("", alan.Asset)
		if err != nil {
			panic(err) // If there's an error, stop the program
		}

		// Use the piper instance to synthesize speech from text
		wavBytes, err := tts.Synthesize(content)
		if err != nil {
			panic(err) // If there's an error, stop the program
		}

		// Create an io.Reader from the byte array
		r := bytes.NewReader(wavBytes)

		// Decode the WAV data into a format that beep can understand
		streamer, format, err := wav.Decode(r)
		if err != nil {
			panic(err) // If there's an error, stop the program
		}

		// Initialize the speaker with the sample rate from the WAV data
		speaker.Init(format.SampleRate, format.SampleRate.N(time.Second/10))

		// Create a done channel to signal when the audio has finished playing
		done := make(chan bool)

		// Play the audio and signal the done channel when finished
		speaker.Play(beep.Seq(streamer, beep.Callback(func() {
			done <- true // Signal the done channel
		})))

		// Wait for the audio to finish playing before allowing the program to exit
		<-done
  },
}

func Execute() {
  if err := rootCmd.Execute(); err != nil {
    fmt.Println(err)
    os.Exit(1)
  }
}