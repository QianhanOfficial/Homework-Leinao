# Final-Homework-Encephaloid
 认知科学与类脑计算-大作业

## 实验环境：

- 安装 Anaconda-22.11.0（Python-3.9.13）
- 操作系统：Windows10
- GPU：NVIDIA RTX 2060

## 1. 安装 Rasa

在项目路径的终端中运行如下命令：

```bash
pip install rasa
```

待 Rasa 安装完成之后，需要配置所需环境：

```bash
pip install rasa[full]
```

上面的命令将安装 Rasa 所需的大部分组件。

## 2. 配置与训练

`config.yml`中给出了本实验所使用的组件。

为了应用这些组件，在项目路径中运行：

```bash
rasa train
```

按照配置信息来训练机器人模型。过程中需要下载组件所需的语言模型（如 BERT 的官方中文语言模型）等内容，可能耗时较长。

训练完成后，将会在`项目路径/models/`中生成一个对话机器人模型。运行时，Rasa 会自动加载其中命名名称中时间最新的模型。

## 3. 运行

首先，在项目路径中运行命令开启 Rasa 服务器：

```bash
rasa run --enable-api
```

参数`--enable-api`表示开启 Rasa 服务器的 HTTP API。

接下来，使用`_connect_rasa.py`连接服务器。

```bash
python -m _connect_rasa.py
```

等待连接完成后，出现输入提示符`Your Input -> `。此时可以正常进行交互了。

语料库中共编写了“打招呼”、“再见”、“闲聊”、“吃饭”、“关心”、“赞美”、“害怕”和“开心”共8个意图的数据，可以参考`项目路径/data/nlu.yml`中的询问内容来进行测试。

退出时可以输入`/stop`来关闭脚本，然后使用`Ctrl+C`关闭 Rasa 服务器。
