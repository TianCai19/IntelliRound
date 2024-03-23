from agentscope.agents import DialogAgent
from agentscope.message import Msg
from agentscope.pipelines.functional import sequentialpipeline
import agentscope
from agentscope.msghub import msghub

# 定义新的代理类，用于圆桌讨论
class DiscussionAgent(DialogAgent):
    def __init__(self, name, gender, age, occupation, education, nationality, worldview, **kwargs):
        # 设置代理的个性化属性
        self.gender = gender
        self.age = age
        self.occupation = occupation
        self.education = education
        self.nationality = nationality
        self.worldview = worldview
        
        # 构造函数需要的参数
        sys_prompt = f"You are a {self.age}-year-old {self.occupation} from {self.nationality} with a {self.worldview} perspective.you are join a table disscussion ,talk with others about the topic.just be yourslf ,say waht u want .In China ,you should say Chinese"
        model_config_name = "qwen"  # 假设我们使用名为'qwen'的模型配置

        # 调用父类的初始化方法
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name, **kwargs)



    
# 初始化AgentScope
agentscope.init(model_configs="./model_configs.json")

import json
agents = []
# 假设你的 JSON 文件名为 agents.json
with open('agents.json', 'r') as file:
    agents_data = json.load(file)['agents']
# 导入代理数据

    for agent_data in agents_data[:3]:
        agents.append(DiscussionAgent(**agent_data))

# 创建代理实例
# agents = [
#     DiscussionAgent("Alice", "Female", 28, "Engineer", "Master's", "American", "Optimistic"),
#     DiscussionAgent("Bob", "Male", 35, "Teacher", "PhD", "Canadian", "Pessimistic"),
#     DiscussionAgent("Charlie", "Non-binary", 22, "Artist", "Bachelor's", "French", "Realistic")
# ]


# 定义讨论话题
topic = "What is the impact of technology on society?"
topic=" 讲个自己领域的笑话"
topic="中国发展对世界的影响"
topic="为啥下一代的教育很重要"
announcemnet = f"hello ,every one ,today table event's topic is {topic} ，answer brefly within 3 sentence.Try using Chinese."

# 开始讨论
# for agent in agents:
#     # 每个代理对话题进行回复
#     agent_response = agent.reply(Msg("Host", topic))
#     print(f"{agent.name}: {agent_response.content}")


x=Msg("Host", "介绍你自己用汉语")
for agent in agents:
    # x = agent(x)
    agent.reply(x)

with msghub(
    participants=agents,announcement=Msg("Host", announcemnet)
) as hub:
    # Agents can now broadcast and receive messages within this block
    x=None

    hub.broadcast(Msg("Host", topic))
    for _ in range(3):
        x = sequentialpipeline(agents, x)
        
        # hub.broadcast(Msg("Host", "感谢大家这一轮的回答，接下来开始下一轮的讨论"))
    