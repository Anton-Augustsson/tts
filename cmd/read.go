package cmd

import (
	"fmt"

	"github.com/Anton-Augustsson/tts/internal/read"
	"github.com/Anton-Augustsson/tts/model"
	"github.com/spf13/cobra"
)

var (
	readCmdsUse = map[string]string{
		"cmdRead": "read",
	}

	text string

	cmdRead = &cobra.Command{
		Use:   readCmdsUse["cmdRead"],
		Short: "Read text or from clipboard",
		Args:  cobra.NoArgs,
		RunE: func(cmd *cobra.Command, args []string) error {
			if text != "" {
				fmt.Println(text)
				return read.Read(text)
			}

			content, err := read.GetContent()
			if err != nil {
				return err
			}
			fmt.Println(content)
			return read.Read(content)
		},
	}
)

func init() {
	cmdRead.Flags().StringVarP(&text, model.Flag.Text.Name, model.Flag.Text.Short, "", model.Flag.Text.Desc)
}
