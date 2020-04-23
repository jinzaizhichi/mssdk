# 安装指导

## 重要提示

1. 首先请确认安装 [Python](https://www.python.org/) 3.6 及以上版本, 这里推荐 [Python](https://www.python.org/) 3.7.5 版本;
2. 推荐 [Anaconda](https://www.anaconda.com/), 可以解决大部分安装问题.

## 安装 mssdk

### 通用安装

```
pip install mssdk  --upgrade
```

### 国内安装-Python

```
pip install mssdk -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com  --upgrade
```

### 国内安装-Anaconda

```
pip install mssdk -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com  --user  --upgrade
```

## 使用 mssdk

### 全局 token 设置

```python
import mssdk as qh
qh.set_token("在此处输入 token，可以联系麦思多维科技管理员获取")
```

如上代码进行设置后，之后在本地调取数据可以直接使用如下代码：

```python
from mssdk import pro_api
pro = pro_api()  # 此处由于全局 token 的设置，在本机不需要再次输入
commodity_flow_long_df = pro.commodity_flow_long(date="2018-08-08")
print(commodity_flow_long_df)
```

### 临时 token 设置

```python
from mssdk import pro_api
pro = pro_api(token="在此处输入您的token，可以通过联系管理员获取")  # 此处 token 仅供临时使用
commodity_flow_long_df = pro.commodity_flow_long(date="2018-08-08")
print(commodity_flow_long_df)
```
