These commands are part of Riccardo's "AI Cinema" Demo Show around Europe in 2025,
built in collaboration with the amazing Hussain, maitainer of MCP Vertex AI GenMedia in golang.

Note that these commands will NOT WORK unless you pre-install MCP `go` packages in `~/go/bin`.

## INSTALL

1. Follow manual instructions in https://github.com/GoogleCloudPlatform/vertex-ai-creative-studio/blob/main/experiments/mcp-genmedia/README.md
2. Or simply ask Gemini: `gemini -p /aicinema:check_install Help me install GenMedia on this machine.`
3. Ensure to log in with `gcloud auth`. Note that the execution of the MCP server is authenticated when it's launched, and from Gemini CLI
   this happens at launch time. If you authenticate AFTER launching Gemini CLI, the MCP from this session will fail until you restart *GianCarlo*.

## About

Allow you to:

1. Check the installation is correct.
2.
