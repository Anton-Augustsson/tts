package read

import (
	"bytes"
	"strings"
	"time"

	"github.com/atotto/clipboard" // Import the piper package for text-to-speech

	"github.com/amitybell/piper" // Import the piper package for text-to-speech
	// jenny "github.com/amitybell/piper-voice-jenny" // Jenny's voice is available but not used in this example
	alan "github.com/amitybell/piper-voice-alan" // Import Alan's voice from the piper package
	"github.com/gopxl/beep"                      // Import the beep package for playing audio
	"github.com/gopxl/beep/speaker"              // Import the speaker package to output the audio
	"github.com/gopxl/beep/wav"                  // Import the wav package to decode the wav audio
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

func GetContent() (string, error) {
	content, err := clipboard.ReadAll()
	if err != nil {
		return content, err
	}
	return content, nil
}

func Read(content string) error {
	tts, err := piper.New("", alan.Asset)
	if err != nil {
		return err
	}

	words := strings.Fields(content)
	chunkSize := 15
	numWords := len(words)
	done := make(chan bool)
	isFirst := true

	for i := 0; i < numWords; i += chunkSize {
		end := i + chunkSize
		if end > numWords {
			end = numWords
		}
		chunk := words[i:end]

		streamer, format, err := prepare(tts, strings.Join(chunk, " "))
		if err != nil {
			return err
		}

		// The first iteration does not use done
		if isFirst {
			go func() {
				done <- true
			}()
			isFirst = false
		}
		<-done

		speaker.Init(format.SampleRate, format.SampleRate.N(time.Second/10))
		done = make(chan bool)
		play(streamer, done)
	}

	<-done
	return nil
}
