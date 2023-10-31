#!/bin/sh

poetry run python -m flask --app chatbot_agent_sandbox/proxy_server.py run -p 4000
