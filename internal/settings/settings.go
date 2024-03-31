package settings

import (
	"log"

	"github.com/Anton-Augustsson/tts/internal/input_verifier"
	"github.com/Anton-Augustsson/tts/model"
)

func SetSettings(language string, voice string, speed float32) error {
	validLanguage, validVoice, err := input_verifier.ValidLanguageParam(language, voice)
	if err != nil {
		return err
	}

	validSpeed, err := input_verifier.ValidSpeed(speed)
	if err != nil {
		return err
	}

	settings := &model.Settings{
		LanguageParam: model.LanguageParam{
			Language: validLanguage,
			Voice:    validVoice,
		},
		Speed: validSpeed,
	}

	log.Println(settings)
	return nil
}
