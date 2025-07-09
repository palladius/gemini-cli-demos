Start by writing to stdout "Runnin Carlessian Cron Job..."

Consolidate `README.md` file according to @GEMINI.md:

1. Check for all demos under `demos/`. For each:
   1. check that `demos/<DIR>/STATUS.md` is current. If not update it based on the content of the folder.
   2. Check that `just test` works, if exists. Again update STATUS.md
   3. Finally, check that `./README.md` has a table line with this demo, and if so that the info there is up to date.

Add to the README a log line like

"""* YYYY-MM-DD HH:MM Last execution of etc/prompts/headless-consolidate-readme.md"""

under the Logs H2 stanza
