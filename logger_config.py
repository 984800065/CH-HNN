"""
Loguru配置模块
配置彩色输出、文件路径和行号显示
"""
from loguru import logger
import sys

# 移除默认的handler
logger.remove()

# 配置格式：包含时间、级别、文件路径:行号和消息
format_string = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{file.path}</cyan>:<cyan>{line}</cyan> | "
    "<level>{message}</level>"
)

# 添加控制台输出handler，启用彩色
logger.add(
    sys.stderr,
    format=format_string,
    level="DEBUG",
    colorize=True,
    backtrace=True,
    diagnose=True
)

# 导出配置好的logger
__all__ = ['logger']

