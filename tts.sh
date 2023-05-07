#!/bin/bash
process=$(ps -aux | grep "mpg123" | sed -n '2 p' | awk '{print $2}')

while getopts 'pkr' OPTION; do
  case "$OPTION" in
    p)
		state=$(ps -aux | grep "mpg123" | sed -n '2 p' | awk '{print $8}')

		echo "pause/play"
		case $state in
			SLl)
				kill -SIGSTOP $process
				echo "pause"
			;;
			TLl)
				kill -SIGCONT $process
				echo "play"
			;;
		esac
		;;
    k)
		kill -SIGINT $process
		echo "kill process"
		;;
    r)
		aatts --read="$(xclip -o)"
		echo "reading"
		;;
    ?)
		echo "script usage: $(basename \$0) [-p] [-k] [-r]" >&2
		exit 1
		;;
  esac
done
shift "$(($OPTIND -1))"
