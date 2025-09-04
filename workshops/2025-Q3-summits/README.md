# Welcome to this beautiful workshop

To do this workshop, you need two things:

1. A GitHub account (optional but recommended)
2. `Gemini CLI` installed. Tranquillo, if you don't, we can work on that.

And of course, a computer connected to the internet.

## Installing Gemini CLI

You can install Gemini CLI on any machine, via `npm/npx`, even `brew` if you're on Mac.

1. Go to https://github.com/google-gemini/gemini-cli
2. Follow instructions.

## Getting started: download the code

If you do have a GitHub account:

1. **Fork** this repo: https://github.com/palladius/gemini-cli-demos
2. `git clone https://github.com/YOUR_USER/gemini-cli-demos`

If you don't have a GitHub account, you can just download the repo

1. Go to https://github.com/palladius/gemini-cli-demos#
2. Click Code > "Download ZIP"
3. You can take it from there.

**Finally** (in the Java sense of the word), you should have the code unzipped/cloned in a local `path/to/gemini-cli-demos`.
If you use a UI, like VSCode, Netbeans, Zed, or so, make sure to open it at the right unzipped/cloned folder, like

* `[code|zed|..] path/to/gemini-cli-demos/`


## The workshop

I hope your energy levels are good! We're getting started!

1. Ensure you have your favorite IDE open (if you use one).
2. ensure to `cd path/to/gemini-cli-demos` if you didnt follow the previous step. You should be in a folder with a `GEMINI.md`, a `README.md`, a `justfile` and other. It's important you call gemini from THIS folder, or scripts wont work!
3. Let's now call `$ gemini` on your local shell.
4. To start the workshop, do something like this: `/workshops:01_create_issue What do you want to do`. Examples:

```bash
# Example 1: app creation
/workshops:01_create_issue I want to vibe code a new app with Astro which tracks clicks from participants. Ensure a github issue tracks this.
# Example 2: git history
/workshops:01_create_issue I want to check the git history of this repo.
# Example 3: disk space
/workshops:01_create_issue Tell me how much disk space do I have? What are the biggest folders and how do i clean them up?
# Example 3: DB
/workshops:01_create_issue Help me create a SQLite DB called workshop-test.db with 3 tables called Orders, Items, Customers. Make sure the tables are linked. Finally create a db_schema.md with a mermaid graph of the schema, and help me commit to the repo.
# Example 3: Planning a new app: PRD + Implementation plan.
/workshops:01_create_issue Help me write the PRD for a new application to track participants clicks, so that the firs click returns a different PIN number. Every click will be tracked (IP, timestamp, PIN given). No login needed. Ask user for a preferred language/framework. If nothing is chosen, use Rails. Track this plan in a markdown and let the user review and commit after the user is happy. Some refinement will be needed. DO NOT IMPLEMENT anything, the output is a clicking-app-plan-PRD.md. When the user is happy, create a MD checklist clicking-app-plan-IMPLEMENTATION.md with the activities that need to be done. Finally commit the two files and link them in a new issue for ease of tracking.
```
Decide the authentication you want to have, the simplest is to use a gmail account login. You can swap auth via `/auth`.

## REMOVEME

ricc pvt doc: https://go/ricc-2025q3-cloud-summits
