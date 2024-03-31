package model

// Verify input should make sure that nothing bad is put into setting
// Then i need to check that the input is an language

// From iso639.1
type Language string
type Voice string

const (
	English Language = "en"
	Swedish Language = "sv"
	German  Language = "de"
)

const (
	Alan     Voice = "alan"
	Cori     Voice = "cori"
	Karlsson Voice = "karlsson"
	Nst      Voice = "nst"
)

var LanguageVoices = map[Language][]Voice{
	English: {Alan, Cori},
	German:  {Karlsson},
	Swedish: {Nst},
	// Add more language-voice mappings as needed
}

type LanguageParam struct {
	Language Language
	Voice    Voice
}
