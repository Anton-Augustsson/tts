package cmd

import (
	"fmt"
	"os"

	"github.com/Anton-Augustsson/tts/internal/read"
	"github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{
	Use:   "aatts-go",
	Short: "Read the latest in clipboard",
	Long: `To select the text you have to Ctrl C the text you want to read.
                Thus it is independent from any program.
                It can also be run on any platform.`,
	RunE: func(cmd *cobra.Command, args []string) error {
		//if len(args) != 0 || cmd.Flags().NFlag() != 0 {
		//	return errors.New("arguments or flags provided for root argument")
		//}
		content, err := read.GetContent()
		if err != nil {
			return err
		}
		return read.Read(content)
	},
}

func Execute() {
	rootCmd.AddCommand(cmdRead, cmdSettings)

	if err := rootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
