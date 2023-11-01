import os
import random
import sys

from dotenv import load_dotenv

if "pytest" in sys.argv or "pytest" in sys.modules or os.getenv("CI"):
    print("Setting random seed to 42")
    random.seed(42)

# Load the users .env file into environment variables
load_dotenv(verbose=True, override=True)
# 这是使用load_dotenv函数加载当前目录下的.env文件。verbose=True表示在加载时输出详细信息，而override=True表示如果存在同名环境变量，则覆盖它们。
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 这行代码是用来获取当前文件所在路径的上级目录的路径。它首先获取当前文件的绝对路径，然后取这个路径的父级和再父级，也就是根路径。这个路径通常用于定义项目的根目录。
load_dotenv(os.path.join(ROOT_PATH, ".plugin_env"))
# 这行代码是在项目的根目录下加载.plugin_env文件。这可能是一个针对特定插件的环境变量文件。
del load_dotenv
# 删除名为load_dotenv的变量。在Python中，当你不再需要一个变量时，通常会使用del语句删除它，以释放内存。
