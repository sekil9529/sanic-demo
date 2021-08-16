# coding: utf-8

import os
from loguru import logger

"""loguru
文档地址：
    1.https://github.com/Delgan/loguru
    2.https://loguru.readthedocs.io/en/stable/api/logger.html#message
"""


def init_log(base_dir: str) -> None:
    log_path = os.path.join(base_dir, 'logs')
    if not os.path.exists(log_path):
        os.mkdir(log_path)

    log_all = os.path.join(log_path, "all.log")
    log_error = os.path.join(log_path, "error.log")

    """
    enqueue:  要记录的消息是否应在到达接收器之前首先通过多进程安全队列。这在通过多个进程记录到文件时很有用。这也具有使日志记录调用非阻塞的优点
        为True时，diagnose必须为False, 否则logger.exception不记录
    serialize: 在发送到接收器之前，是否应首先将记录的消息及其记录转换为 JSON 字符串
    rotation ( str, int, datetime.time, datetime.timedeltaor callable, optional) – 一种条件，指示何时应关闭当前记录的文件并开始新的文件
    retention (str, int, datetime.timedelta or callable, optional) – 过滤旧文件的指令，应在循环或程序结束期间删除
    backtrace ( bool, 可选) – 格式化的异常跟踪是否应该向上扩展，超出捕获点，以显示生成错误的完整堆栈跟踪
    diagnose（bool，可选）– 异常跟踪是否应显示变量值以简化调试。生产环境中应该设置为False避免泄露敏感数据
    """
    format_str = "[{time:YYYY-MM-DD HH:mm:ss.SSSSSS}] - [{level}] - [{name}:{line}] - [{message}]"
    logger.add(log_all, level='INFO', format=format_str, rotation='0:00', enqueue=True,
               serialize=False, encoding='utf-8', retention='10 days', backtrace=False, diagnose=False)
    logger.add(log_error, level='ERROR', format=format_str, rotation='0:00', enqueue=True,
               serialize=False, encoding='utf-8', retention='10 days', backtrace=False, diagnose=False)
