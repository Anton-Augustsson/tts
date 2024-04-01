package cmd

import (
	"github.com/Anton-Augustsson/tts/internal/settings"
	"github.com/Anton-Augustsson/tts/model"
	"github.com/spf13/cobra"
)

var (
	settingsCmdsUse = map[string]string{
		"cmdSettings":     "settings",
		"cmdSettingsSet":  "set",
		"cmdSettingsList": "list",
	}

	language string
	voice    string
	speed    float32

	cmdSettings = &cobra.Command{
		Use: settingsCmdsUse["cmdSettings"],
	}

	cmdSettingsSet = &cobra.Command{
		Use:   settingsCmdsUse["cmdSettingsSet"],
		Short: "Modify your settings",
		Long:  `Set your language, voice, and speed. The changes are persistent and will be saved for `,
		Args:  cobra.NoArgs,
		RunE: func(cmd *cobra.Command, args []string) error {
			return settings.SetSettings(language, voice, speed)
		},
	}

	cmdSettingsList = &cobra.Command{
		Use:   settingsCmdsUse["cmdSettingsList"],
		Short: "List your settings",
		Args:  cobra.NoArgs,
		RunE: func(cmd *cobra.Command, args []string) error {
			// TODO: read from persistent file
			return nil
		},
	}
)

func init() {
	cmdSettings.AddCommand(cmdSettingsSet)
	cmdSettings.AddCommand(cmdSettingsList)

	cmdSettingsSet.Flags().StringVarP(&language, model.Flag.Language.Name, model.Flag.Language.Short, "en", model.Flag.Language.Desc)
	cmdSettingsSet.Flags().StringVarP(&voice, model.Flag.Voice.Name, model.Flag.Voice.Short, "alan", model.Flag.Voice.Desc)
	cmdSettingsSet.Flags().Float32VarP(&speed, model.Flag.Speed.Name, model.Flag.Speed.Short, 1.0, model.Flag.Speed.Desc)

}
