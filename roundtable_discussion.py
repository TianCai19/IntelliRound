from agentscope.agents import DialogAgent
from agentscope.message import Msg
from agentscope.pipelines.functional import sequentialpipeline
import agentscope
from agentscope.msghub import msghub
import json

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



    
def start_roundtable_discussion(topic="What is the impact of technology on society?", rounds=3):
    # 初始化AgentScope
    agentscope.init(model_configs="./model_configs.json")

    agents = []
    # 假设你的 JSON 文件名为 agents.json
    with open('agents.json', 'r') as file:
        agents_data = json.load(file)['agents']
    
    for agent_data in agents_data[:3]:
        agents.append(DiscussionAgent(**agent_data))

    # 定义讨论话题
    announcemnet = f"Hello everyone, today's table event's topic is {topic}. Please answer briefly within 3 sentences."

    with msghub(
        participants=agents, announcement=Msg("Host", announcemnet)
    ) as hub:
        # Agents can now broadcast and receive messages within this block
        x = None

        hub.broadcast(Msg("Host", topic))
        for _ in range(rounds):
            for agent in agents:
                x = agent(x)
