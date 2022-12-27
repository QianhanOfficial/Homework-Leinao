import json # 使用json连接rasa server
import secrets # 用于生成会话id
import requests # 用于post方法

# post方法传输rasa的回复
def post(url, data=None):
    data = json.dumps(data, ensure_ascii=False)
    data = data.encode(encoding="utf-8")
    r = requests.post(url=url, data=data) # post
    r = json.loads(r.text) # 读取文本
    return r

# 接下来链接rasa server
conversation_id = secrets.token_urlsafe(16) # 随机生成会话id
# rasa接收输入消息的地址
messages_url = "http://localhost:5005/conversations/{}/messages".format(conversation_id) 
# 这里是rasa NLU server处理得到的特征结果，可以取出分类得到的意图对应的Action
predict_url = "http://localhost:5005/conversations/{}/predict".format(conversation_id) 
# 这里是rasa自动处理得到的执行结果，这里可以取出回复文本response
execute_url = "http://localhost:5005/conversations/{}/execute".format(conversation_id)

# 初始化动作为监听
action = "action_listen"
while True:
    if action in ["action_listen", "action_default_fallback", "action_restart"]:
        # 等待输入
        text = input("Your input -> ")
        if text == "/stop": # 结束连接
            exit()
        post(messages_url, data={"text": text, "sender": "user"})  # 发送消息
        

    response = post(predict_url)  # 预测下一步动作
    action = response["scores"][0]["action"]  # 取出置信度最高的下一步动作

    response = post(execute_url, data={"name": action})  # 执行动作
    messages = response["messages"]  # 取出对话信息
    
    # 处理rasa的response消息
    if messages:
        text = messages[0]["text"] # 取出文本
        print(text) # 输出文本到shell