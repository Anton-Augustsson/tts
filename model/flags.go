package model

type OurFlag struct {
	Name  string
	Short string
	Desc  string
}

type Flags struct {
	Language OurFlag
	Voice    OurFlag
	Speed    OurFlag
	Text     OurFlag
}

var Flag = Flags{
	Language: OurFlag{
		Name:  "lang",
		Short: "l",
		Desc:  "the language you want to use using ISO 639-1 abbreviation",
	},
	Voice: OurFlag{
		Name:  "voice",
		Short: "v",
		Desc:  "the voice you want to use for the language",
	},
	Speed: OurFlag{
		Name:  "speed",
		Short: "s",
		Desc:  "the speed you want to use when reading",
	},
	Text: OurFlag{
		Name:  "text",
		Short: "t",
		Desc:  "the text you want to read",
	},
}
