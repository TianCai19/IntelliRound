from agentscope.agents import DialogAgent
from agentscope.message import Msg
from agentscope.pipelines.functional import sequentialpipeline
import agentscope

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
        sys_prompt = f"You are a {self.age}-year-old {self.occupation} from {self.nationality} with a {self.worldview} perspective. "
        model_config_name = "qwen"  # 假设我们使用名为'qwen'的模型配置

        # 调用父类的初始化方法
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name, **kwargs)



    
# 初始化AgentScope
agentscope.init(model_configs="./model_configs.json")

# 创建代理实例
agents = [
    DiscussionAgent("Alice", "Female", 28, "Engineer", "Master's", "American", "Optimistic"),
    DiscussionAgent("Bob", "Male", 35, "Teacher", "PhD", "Canadian", "Pessimistic"),
    DiscussionAgent("Charlie", "Non-binary", 22, "Artist", "Bachelor's", "French", "Realistic")
]

# 定义讨论话题
topic = "hello ,every one ,today table event's topic is What is the impact of technology on society?,answer brefly within 3 sentence.using english "

# 开始讨论
for agent in agents:
    # 每个代理对话题进行回复
    agent_response = agent.reply(Msg("Host", topic))
    print(f"{agent.name}: {agent_response.content}")