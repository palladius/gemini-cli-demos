One of the things GC is good at, is looking at your local File System
and running commands like a real Linux pro. I thought I was quite good at it, but who knows all the right git commands for the job? Surely I DONT.

# Steps

Let's try to play around with git in this local repo to show case some of the abilities it has.

## Step 1

1. You wonder "who the hell created this file or folder, and more imporantly. WHY?" I think a smart git command could answer both questions. They can find hidden correlations that a human would take ageds to find. For instance:

```markdown
who the hell created assets/ folder, and in which commit,
and what were they trying to achieve?
```

## Step 2

2. Maybe we can create a nice graph in `git_history.md`, maybe this can be run as a one off or as a script :) Sometimes you want to script for things, sometimes you just want to vibe it - maybe it's a one off.

```markdown
Write a file called `git_history.md` which contains:
1. A bullet points with `commit_hash` and a one line short description of the commit. Summarize if needed.
2. Create a mermaid graph of all the links between them so I can see this in a `gitk`-like rendering.
```

## Step 3


3. create a script for the above - to make it deterministic (avoid summarization, jusyt truncate to first 70 chars.)


## Step 4

Maybe you have someone who broke the system in a nonobvious way, or did a major refactor you want to surgically remove? - how about creating `git bisect` to solve this for you? Or auto-de-merging some code/commit (good luck with this).
