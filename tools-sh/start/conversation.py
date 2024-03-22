# -*- coding: utf-8 -*-
"""A simple example for conversation between user and assistant agent."""
import agentscope
from agentscope.agents import DialogAgent
from agentscope.agents.user_agent import UserAgent
from agentscope.pipelines.functional import sequentialpipeline


def main() -> None:
    """A conversation demo"""

    agentscope.init(
        model_configs=[
       {
            "model_type": "gemini_chat",
            "config_name": "gemini",
            "model": "gemini-pro",
            "api_key": "AIzaSyD28CiLXcwzIiycOiDi81XsnmGhZ3b76aU",  # Load from env if not provided
            "organization": "xxx",  # Load from env if not provided
            "generate_args": {
                "temperature": 0.5,
            },
        }

        ],
    )

    # Init two agents
    dialog_agent = DialogAgent(
        name="Assistant",
        sys_prompt="You're a helpful assistant.",
        model_config_name="gemini",  # replace by your model config name
    )
    user_agent = UserAgent()

    # start the conversation between user and assistant
    x = None
    while x is None or x.content != "exit":
        x = sequentialpipeline([dialog_agent, user_agent], x)


if __name__ == "__main__":
    main()
