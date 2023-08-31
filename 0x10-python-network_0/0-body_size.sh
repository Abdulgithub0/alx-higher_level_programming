#!/usr/bin/env bash
# a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
if [ $# -ge 1 ]; then
	curl -sI "$1" | grep "Content-Length" | sed "s/[^0-9]*//"
fi
