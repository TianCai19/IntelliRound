# first configuration dicctionary
# config init
from agentscope.message import Msg
import agentscope
from agentscope.agents import DialogAgent, UserAgent

agentscope.init(model_configs= './model_configs.json')

# Create a dialog agent and  user agent
dialogAgent = DialogAgent(name="Ac", model_config_name="qwen", sys_prompt="You are a helpful ai assistant")
userAgent = UserAgent()
dialogAgentB= DialogAgent(name="Ab", model_config_name="moonshot", sys_prompt="You are a helpful ai assistant")

#message_from_alice = Msg("Alice", "Hi!")
#print(message_from_alice)

x = None
while True:
   # x = dialogAgent(x)
    x = dialogAgent(x)
    print("x:", x)
    x = userAgent(x)

    # Terminate the conversation if the user types "exit"
    if x.content == "exit":
        print("Exiting the conversation.")
        break