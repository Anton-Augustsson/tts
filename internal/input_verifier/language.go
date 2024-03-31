package input_verifier

import (
	"errors"

	"github.com/Anton-Augustsson/tts/model"
)

func ValidLanguageParam(language string, voice string) (model.Language, model.Voice, error) {
	languageToCheck := model.Language(language)
	voiceToCheck := model.Voice(voice)

	supportedVoices := model.LanguageVoices[languageToCheck]
	if len(supportedVoices) == 0 {
		return languageToCheck, voiceToCheck, errors.New("invalid language")
	}

	for _, supportedVoice := range supportedVoices {
		if supportedVoice == voiceToCheck {
			return languageToCheck, voiceToCheck, nil
		}
	}

	return languageToCheck, voiceToCheck, errors.New("invalid voice")
}
