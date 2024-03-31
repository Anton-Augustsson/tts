package cmd

import (
	"github.com/Anton-Augustsson/tts/internal/read"
	"github.com/Anton-Augustsson/tts/model"
	"github.com/spf13/cobra"
)

var (
	readCmdsUse = map[string]string{
		"cmdRead": "read",
	}

	cmdRead = &cobra.Command{
		Use:   readCmdsUse["cmdRead"],
		Short: "Modify your settings",
		Long:  `Set your language speed and more. The changes are persistent and will be saved for `,
		RunE: func(cmd *cobra.Command, args []string) error {
			content, err := read.GetContent()
			if err != nil {
				return err
			}
			return read.Read(content)
		},
	}
)

func init() {
	cmdRead.Flags().StringP(model.Flag.Text.Name, model.Flag.Text.Short, "", model.Flag.Text.Desc)
}
