# Gemini CLI *beautiful* workshop

<table border="0">
  <tr>
    <td valign="top">
      <p>To do this workshop, you need two things:</p>
      <ol>
        <li>A GitHub account (optional but recommended, for forks and PRs).</li>
        <li><code>Gemini CLI</code> installed. Tranquillo, if you don't, we can work on that.</li>
      </ol>
      <p>And of course, a computer connected to the 🛜 internet.</p>
    </td>
    <td width="50%" align="center">
      <img src="images/image-2.png" alt="A beautiful workshop">
    </td>
  </tr>
</table>

<!-- ![Beautiful Workshop](image.png) -->


## Prerequisites: Installing Gemini CLI

You can install Gemini CLI on any machine, via `npm/npx`, even `brew` if you're on Mac.

1. Go to https://github.com/google-gemini/gemini-cli
2. Follow instructions.
3. It also helps to have these installed:
   1. [jq](https://jqlang.org/) (needed for the custom command)
   2. [just](https://github.com/casey/just) (optional).

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

Decide the authentication you want to have, the simplest is to use a **gmail account login**.
You can swap auth via `/auth`.

## The workshop

I hope your energy levels are good! We're getting started!

1. Ensure you have your favorite IDE open (if you use one).
2. ensure to `cd path/to/gemini-cli-demos` if you didnt follow the previous step. You should be in a folder with a `GEMINI.md`, a `README.md`, a `justfile` and other. It's important you call gemini from THIS folder, or scripts wont work!
3. Let's now call `$ gemini` on your local shell.

### 1. Our first interactions

What's this code? I don't know! Let's ask Gemini!

Copy and paste the following question (or something similar):

```bash
Explain the `workshops/2025-Q3-summits/ code base`.
What does it do?
```

Now type this (don't forget the '@' symbol):

```
Read @workshops/2025-Q3-summits/GEMINI.md
```

This enforces the reading of a GEMINI.md prompt, which changes Gemini's behaviour. Now it should start using emojis and a few German words.

Finally, ask ANY question! Something like:

```
What is the workshop of today?
What is Riccardo's favourite ice cream?
```

### 2. Our first custom command

Type:  `/workshops:01_create_issue`. This should be very straightforward and should lead you to creating an issue under https://github.com/palladius/gemini-cli-demos/issues , hopefully with a [WS01](https://github.com/palladius/gemini-cli-demos/issues?q=is%3Aissue%20state%3Aopen%20label%3Aws01) label.

![ws02](image.png)

### 3. Our second custom command (dangerous!)

We have created a strange and dangerous "sign me up" functionality which will likely result in a Merge request nightmare.

Do something like this: `/workshops:02_add_me_to_class in Cloud Summit Zurich`.

* Follow the lead of Gemini CLI who should guide you through the generation of a YAML (make sure you share info you want to share!)
* Follow the guide to the creation of a [Pull Request](https://github.com/palladius/gemini-cli-demos/pulls).

<!-- This is obsolete now, but i might resurrect it someday in the near future
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
-->

![this is optional](image-2.png)

## 3. [optional] Now your turn to create automation!

Did you like what you see? Now you can start experimenting yourself!

### [optional] Move to YOUR OWN repo!

Want to apply this to your own repo? Very simple!

```
# CD to your repo.
$ cd path/to/your_own_repo/
$ gemini
```

If no repos available, you can always clone some juicy ones: [Microservices Demo](https://github.com/GoogleCloudPlatform/microservices-demo), or [Bank of Anthos](https://github.com/GoogleCloudPlatform/bank-of-anthos).

Then ask questions like:

```
"What does this repo do?"

"show me what I did in the latest commit"

"Which files were changed in the past 24h?"

"Write a doc/ABOUT.md about what this repo does. Make sure to include a mermaid graph of the relationship between Classes/DB Tables/.."

```
### [optional]  Write your own `GEMINI.md`

Did you notice some aspect where Gemini misbehaved? Or you want to extend/improve something? time to create your first GEMINI.md!

1. Create a GEMINI.md in the root folder or your git repo or edit the existing one.
2. Add some sentences. Something as simple as "Speak to me in Italian" or "add some emoji" or "call me Aladeen" or "substitute both YES and NO with the word Aladeen", or something more pertinent to your coding flow ("Ensure unit tests are there", "Before committing, always remember to run local tests", ..)
3. Now reload `gemini` or run a `/memory refresh` or say "Please re-read @GEMINI.md". Don't forget the at ('@')!

### [optional]  Write your own Custom command

Did you enjoy my Custom commands, like `/workshops:01_create_issue` ? Time to write your own!

1. Check `.commands/commands/`. Look around for files: `find .commands/commands/`. Check also [workshops/01_create_issue.toml](https://github.com/palladius/gemini-cli-demos/blob/main/.gemini/commands/workshops/01_create_issue.toml) itself!
2. Create your own like `.commands/commands/YOURNAME/my_first_cmd.toml`. Say your name is "Julia", something like: `.commands/commands/julia/my_first_cmd.toml`.
3. Check any other TOML in there, as you can see you need to have a `description` and a `prompt`. Add your business logic to the prompt. Also use `{{args}}` to paste what the user will give you when invoking the command.
4. Once you're happy, restart `gemini`.
5. Try writing `/julia:my_first_cmd yellow is my favorite color` (or any other comment).
6. Enjoy Gemini following instructions in your TOML prompt, substituting "yellow is my favorite color" to the {{args}}.
7. Test this also in headless mode! just run `gemini -p "/julia:my_first_cmd yellow is my favorite color"`. Note you might want to give your command some super powers. `--yolo` will let it do ANYTHING (dangerous), a good compromise might be '--approval-mode auto_edit'. More docs [here](https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/shell.md).

### [optional] Add GitHub integration

If you own your own repo, you can add custom GitHub Actions which allow you to interact with your GH repo!

1. Type: `/setup-github`
2. Follow instructions (install the gemini-cli bot, add GEMINI API KEY to your repo, ..)
3. Test it by creating an issue and typing something like `@gemini-cli help me fix this issue`.
4. Enjoy the experience:

![testing gemini-cli GHA](images/gha.png)

### [optional] Add MCP servers!

We haven't had time to explore this in this short workshop, but this is probably the most useful and fascinating aspect.

Some pointers:

* [Use MCP with Gemini CLI](https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md)
* You can add STDIO or HTTP servers as simply as that:
  * `gemini mcp add my-stdio-server -e API_KEY=123 /path/to/server`
  * `gemini mcp add --transport http http-server https://api.example.com/mcp/`
* My favorite MCPs:
  * https://github.com/GoogleCloudPlatform/vertex-ai-creative-studio/tree/main/experiments/mcp-genmedia
  * [Playwright](https://github.com/microsoft/playwright-mcp)
  * [Context7](https://github.com/upstash/context7). Eg
```json
// Add to your .gemini/settings.json
{
  "mcpServers": {
    "context7": {
      "httpUrl": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "YOUR_API_KEY", // Also works from ENV/.env
        "Accept": "application/json, text/event-stream"
      }
    }
  }
}
```

  * [Cloud Run](https://github.com/GoogleCloudPlatform/cloud-run-mcp)

Check if it works:

* Restart `gemini` to pick up the MCP server configs
* Type '/mcp'. Example:

![MCP server](image-1.png)

<!--
Riccardo Only: ricc pvt doc: https://go/ricc-2025q3-cloud-summits
-->
