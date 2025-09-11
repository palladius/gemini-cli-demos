

## Install


```bash
git clone https://github.com/GoogleCloudPlatform/vertex-ai-creative-studio/
cd ./experiments/mcp-genmedia/mcp-genmedia-go
export PROJECT_ID=your-project-id ./install.sh
```

once done

```bash
export PATH=~/go/bin/:$PATH
```

then login:

```bash
gcloud config set account ACCOUNT
gcloud config set project PROJECT_ID
just auth2
```
