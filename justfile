
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

# run gemini CLI - todo use n pm after launch
run:
    npx https://github.com/google-gemini/gemini-cli

# CICD example
update-readme:
    gemini -a -p "Update README with [possibly new] articles under demos/"

# checks that yaml works.
test-yaml-ok:
     cat output/data.yaml  | yq


gemini-consolidate-readme:
    # DOESNT WORK THIS ONE gemini -y -d -p etc/prompts/headless-consolidate-readme.md
    gemini -y -d -p 'Execute commands in this prompt: etc/prompts/headless-consolidate-readme.md'
