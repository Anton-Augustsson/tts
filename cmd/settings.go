package cmd

import (
	"github.com/Anton-Augustsson/tts/internal/settings"
	"github.com/Anton-Augustsson/tts/model"
	"github.com/spf13/cobra"
)

var (
	settingsCmdsUse = map[string]string{
		"cmdSettings": "settings [language] [voice] [speed]",
	}

	cmdSettings = &cobra.Command{
		Use:   settingsCmdsUse["cmdSettings"],
		Short: "Modify your settings",
		Long:  `Set your language speed and more. The changes are persistent and will be saved for `,
		RunE: func(cmd *cobra.Command, args []string) error {
			return settings.SetSettings("en", "alan", 1)
		},
	}
)

func init() {
	cmdSettings.Flags().StringP(model.Flag.Language.Name, model.Flag.Language.Short, "", model.Flag.Language.Desc)
	cmdSettings.Flags().StringP(model.Flag.Voice.Name, model.Flag.Voice.Short, "", model.Flag.Voice.Desc)
	cmdSettings.Flags().StringP(model.Flag.Speed.Name, model.Flag.Speed.Short, "", model.Flag.Speed.Desc)
}
