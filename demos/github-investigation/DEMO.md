

# setup


```
just setup
just download-random-repo
# Starts Gemini CLI vanilla, with no MCP and Extension
giancarlo-permissive-nomcp 
```


## Ideas

1. Git histroy

```
Explain git history of last 3 days of the downloaded repo. Anything from Allen or Riccardo? 
```

2. Repo exploration

```
Create a small `ABOUT.md` explaining what the random repo does. Plus add a small table with relevant info (git repo on github, stars, and other key values you deem important).
```

## Table: Commits per month

```
* How many commits in the past month? Show me a table with committers with a top 10 of Top committers, as you'd do in group by/count in sql.
* Try to improvise a third column with their nationality (italian flag for an italian name, german flag for a german one, american name for english name..). this is just for fun, for a demo, dont overthink it: I'm aware of the possible mistakes.
* Put this into a file: `TopCommittersForFun.md`
```

Explain how this, like a colab, allows you to dump "semilavorati" into files to then resuscitate later on.

## Complex investigation: git history + code semantics

1. Investigate and 2. fix:

```markdown
<!-- 1. Investigation -->
I’ve heard they deprecated the -c (Checkpoint) command, I’m so sad! Can you find in which commit this happened and give me committer, timestamp and GH issue? 

<!-- 2. Fix and PR - actionable! -->
Also I believe the docs still points to this deprecated command, can you help me file a PR to update the docs and reflect the new status?
```