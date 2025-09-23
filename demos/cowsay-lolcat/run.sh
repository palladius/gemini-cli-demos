#!/bin/bash

# Check if cowsay and lolcat are installed
if ! command -v cowsay &> /dev/null || ! command -v lolcat &> /dev/null; then
    echo "Please install cowsay and lolcat to run this demo."
    exit 1
fi

cowsay "Hello from Gemini CLI!" | lolcat
