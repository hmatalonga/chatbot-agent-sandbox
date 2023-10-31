import os
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent

_ = load_dotenv()

# create an AssistantAgent instance named "assistant"
assistant = AssistantAgent(
    name="assistant",
    llm_config={
        "request_timeout": 600,
        "seed": 42,
        "config_list": [
            {
                # "api_type": "open_ai",
                "api_key": "NULL",  # just a placeholder
                "api_base": "http://localhost:4000"
            }
        ],
        "temperature": 0,
    },
)

# create a UserProxyAgent instance named "user_proxy"
user_proxy = UserProxyAgent(name="user_proxy")

# the assistant receives a message from the user, which contains the task description
user_proxy.initiate_chat(
    assistant,
    message="""What date is today? Which big tech stock has the largest year-to-date gain this year? How much is the gain?""",
)
