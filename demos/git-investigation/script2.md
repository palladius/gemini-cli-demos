# About

This script downloads `palladius/vibecoding`, vibe-coded by the author, and tries to find when a problematic library was introduced. The author uses

# Prep

```bash
$ cd demos/git-investigation
$ just vibecoding-copy # downloads the git repo locally to play with it
```

# Prompts

## Intro & first info gathering

I’ve checked an OSS repo, `vibecoding-copy` . If I didn't, please execute "just vibecoding-copy" to download it locally.
Enter that folder and tell me something about it, like when the repo was created, how many committers, how many commits, etc.

## The Prisma problem

Ok, now this project was doing super well until an LLM I won’t mention decided to use some sort of Prisma library to do some database things.
As you can see I’m not good with Javascript or Typescript. I need a favour from you:

1. Identify in which commit that library was introduced - I trust you on how to execute this, maybe some laser focused grepping..
2. Check from the diffs of the previous commit, that commit and the one after (-1, 0, +1) why oh why you did this. Try to understand why.
3. Finally, propose in a “RICCARDO_HATES_PRISMA.md” some alternative libraries and solutions to fix this. Also explain the complexity in removing prisma and use something else.

## Now fix it!

Ok, so now I’ll take your suggestion. Let’s try to change prisma for better-sqlite3 (the original) in the “apps-portfolio” app/folder. Please enter the repo, create a feature branch called “YYYYMMDD-prisma-revert-2-bettersqlite”. Do all the changes there until it works:

- “just test” works
- “just import” works

Finally file a PR on github for this change to happen, and the code to be reviewed by owner.

## Now make a PR

now teach me to make this a Pull Request. Can you do it with gh?

## Now a graph of commits

great. Now finally build me a calendar with Every day since the inception of the project, and for every day I want to see the # commits and the main feature/bug implemented on that day. Show
that graphically for me in output/calendar.md  . The commit shall be in backticks and possibly linked to the commit on github. The commit should be prepended by HH:MM of time of day of the commit, and every commit should be kept short (~1 line): abbreviate if longer than say 100char.
