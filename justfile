
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

# Executes custom command Whareabouts from Riccardo
gemini-whereabouts:
    gemini -y -p /common:whereabout

# Checks for License for sub-folder FOLDER, eg demos/git-investigation/
gemini-check-google-license FOLDER:
    gemini -y -p "/common/check-google-license Verify all is in place for folder {{FOLDER}}, and if needed apply the addlicense script to the whole git repo. Also update STATUS.md"

# New Gemini feature from 28aug25 - auto edit!
gemini:
    gemini -c --approval-mode auto_edit

# Tests the workshop in NON-interactive way.
gemini-workshop:
    gemini -c -y -p "/workshops:01_create_issue DO NOT ASK QUESTION - youve being running in non-interactive mode."
