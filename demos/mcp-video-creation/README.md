# Cinema at home with Gemini CLI!

## Install

Installation will take you some time. But trust me, it IS worth it!

You need to install all golang MCP servers into `~/go/bin/`, eg
`~/go/bin/mcp-imagen-go` for generating images. Then you can have Gemini CLI pick them up, and use them in `stdio` mode.

```bash
git clone https://github.com/GoogleCloudPlatform/vertex-ai-creative-studio/
cd ./experiments/mcp-genmedia/mcp-genmedia-go
export PROJECT_ID=your-project-id ./install.sh
```

once done:

```bash
export PATH=~/go/bin/:$PATH
```

then login:

```bash
gcloud config set account ACCOUNT
gcloud config set project PROJECT_ID
just auth2
```

### Thanks

Thanks to Hussain Chinoy without whose work this wouldn't have been possible.

**GenMedia** rocks!
