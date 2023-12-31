# 🤖 Chatbot Agent Sandbox
> An experiment with LLM agents

## 📦 Apps

1. **💬 Chatbot Basic** - Basic sandbox to interact with GPT3.5 Turbo model
2. **🔎 Chatbot Search** - A search-enabled chatbot via DuckDuckGo Search Engine
3. **🦜 LangChain: Chat with search** - Search chat with history memory with Langchain
4. **🤖 Chatbot Basic System** - Basic sandbox to interact with GPT3.5 Turbo using system prompt
5. **🏺 Chatbot Local Server** - Sandbox running locally via Ollama supports Llama models and other open-source models

## 🧰 Setup

### Requirements
- Python 3.10
- Docker
- Poetry (for local development)

### Install
```shell
$ cp .env.example .env  # fill in credentials
```

## 💡 Usage

### Streamlit Pages

Via Docker (recommended):
```shell
$ docker compose up
```

If you prefer, to run it locally on the host machine:
```shell
$ poetry run streamlit run chatbot_agent_sandbox/ui/0_🏠_Home.py
```

### Agents

Start Ollama model server:
```shell
$ docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama-cpu ollama/ollama  # CPU only
$ docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama-gpu ollama/ollama  # GPU
```

Deploy Openai compatible proxy-server:
```shell
$ poetry run python -m flask --app chatbot_agent_sandbox/proxy_server.py run -p 4000
```

Run agent code:
```shell
$ poetry run python chatbot_agent_sandbox/agents/simple_agent.py
```

## 🔗 References

1. [🎈 Streamlit + LLM Examples App](https://github.com/streamlit/llm-examples)
2. [🦜️🔗 LangChain 🤝 Streamlit agent examples](https://github.com/langchain-ai/streamlit-agent)
3. [🚅 LiteLLM](https://docs.litellm.ai/)
4. [🦙 Ollama](https://ollama.ai/)
5. [🥁 AutoGen](https://microsoft.github.io/autogen/)