
# lists targets
list:
    just -l

# install gemini CLI
install:
    npx https://github.com/google-gemini/gemini-cli


# TODO use gemini cli to ensure quality of a certain demo.
test my_demo:
    echo "ensure quality of my demo: {{my_demo}}" | cat

commit-and-push:
    echo 'commit and push after checking quality gates' | gemini --yolo
