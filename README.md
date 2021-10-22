# sanic-demo
sanic 模板，sanic + tortoise-orm + aiomysql + aioredis

# 环境

- Python-3.7.10
    - sanic==21.9.1
    - aiomysql==0.0.21
    - tortoise-orm==0.17.8
    - aioredis==2.0.0

# 文件组织结构

```
.sanic-demo
├── app                       # app
│   ├── __init__.py
│   ├── blue.py               # 总蓝图
│   ├── demo                  # demo模块
│   │   ├── __init__.py
│   │   ├── blue.py           # demo蓝图
│   │   └── views.py          # demo视图
│   ├── models.py             # tortiose-orm模型
│   └── user                  # 用户模块
│       ├── __init__.py
│       ├── blue.py           # 用户蓝图
│       └── views.py          # 用户视图
├── settings                  # 配置
│   ├── __init__.py           # 获取配置方法
│   ├── base.py               # 配置基类
│   ├── development.py        # 开发环境配置
│   └── production.py         # 生产环境配置
├── core
│   ├── error_code.py         # 错误码
│   ├── exception_handlers    # 异常处理器
│   │   ├── base.py           # 异常处理基类
│   │   ├── error_code.py     # 错误码异常处理
│   │   ├── __init__.py
│   │   └── unknown.py        # 未知异常处理
│   ├── __init__.py
│   ├── listeners             # 监听
│   │   ├── __init__.py
│   │   └── base.py           # 监听基类
│   ├── middlewares           # 中间件
│   │   ├── base.py           # 中间件基类
│   │   ├── __init__.py
│   │   └── timer.py          # 计时中间件
│   └── response.py           # 响应函数
├── libs                      # 公共库
│   ├── config.py             # 配置文件处理方法
│   ├── error_code            # 错误码处理
│   │   ├── __init__.py
│   │   ├── enum.py           # 错误码枚举
│   │   └── exception.py      # 错误码异常
│   ├── __init__.py
│   ├── logger.py             # logger
│   └── secret_key.py         # 生成secret_key方法
├── logs                      # 日志文件存储路径
├── manage.py                 # 启动文件
├── .env_bak                  # 配置文件模板，需要拷贝为.env
└── requirements.txt
```