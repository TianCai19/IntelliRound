import agentscope
from agentscope.agents import DialogAgent, UserAgent
from agentscope.message import Msg
from agentscope.pipelines.functional import sequentialpipeline



# 定义代理类，每个代理都有自己的属性
class CustomAgent(DialogAgent):
    def __init__(self, name, gender, age, occupation, education, nationality, worldview, **kwargs):
        self.gender = gender
        self.age = age
        self.occupation = occupation
        self.education = education
        self.nationality = nationality
        self.worldview = worldview
        self.sys_prompt = f"You are a {self.age}-year-old {self.occupation} from {self.nationality}."
        self.model_config_name = "qwen"
        super().__init__(name=name, **kwargs,sys_prompt=self.sys_prompt, model_config_name=self.model_config_name)



    def reply(self, x):
        # 根据代理的属性生成个性化的回复
        message = f"Hello, I'm {self.name}, a {self.age}-year-old {self.occupation} from {self.nationality}. I think..."
        return Msg(self.name, message)

agentscope.init(model_configs= './model_configs.json')


# 创建代理实例
agents = [
    CustomAgent("Alice", "Female", 28, "Engineer", "Master's", "American", "Optimistic"),
    CustomAgent("Bob", "Male", 35, "Teacher", "PhD", "Canadian", "Pessimistic"),
    CustomAgent("Charlie", "Non-binary", 22, "Artist", "Bachelor's", "French", "Realistic"),
    # ... 添加更多代理
]

# 创建主持人代理
host = UserAgent(name="Host")

# # 初始化AgentScope
# agentscope.init(agent_configs=[{"class": "CustomAgent", "args": {"name": "Host", "sys_prompt": "You are the host of the discussion."}}],
#                 model_configs="./model_configs.json")

# 定义讨论话题和轮数
topic = "What is the impact of technology on society?"
rounds = 10

# 开始讨论
for i in range(rounds):
    print(f"\nRound {i+1} of discussion on {topic}:")
    for agent in agents:
        # 每个代理对话题进行回复
        message = agent(Msg(host.name, topic))
        print(f"{agent.name}: {message.content}")
        # 主持人记录代理的回复
        host(Msg(agent.name, message.content))

# 主持人总结讨论结果
summary = host.reply()
print(f"\nSummary by the Host: {summary.content}")