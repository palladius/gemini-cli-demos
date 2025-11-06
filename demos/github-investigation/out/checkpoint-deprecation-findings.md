# Checkpoint Command Deprecation Findings

I've investigated the deprecation of the `-c`/`--checkpoint` CLI command and found the following information:

## Commit Details

*   **Commit Hash:** `be25e2cb96f8e1e5fed5b3bf2b6547cca707cc63`
*   **Committer:** Allen Hutchison <adh@google.com>
*   **Date:** Fri Oct 17 08:58:00 2025 -0700

## GitHub Information

*   **Pull Request:** [#11338](https://github.com/google-gemini/gemini-cli/pull/11338)
*   **Commit Permalink:** [be25e2c](https://github.com/google-gemini/gemini-cli/commit/be25e2cb96f8e1e5fed5b3bf2b6547cca707cc63)

## Summary

The `--checkpointing` flag was removed in commit `be25e2cb96f8e1e5fed5b3bf2b6547cca707cc63` as part of a larger effort to remove deprecated flags. The functionality is now managed through the `general.checkpointing.enabled` setting in `settings.json`.