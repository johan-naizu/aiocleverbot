![aiocleverbot](https://i.imgur.com/HEskou1.jpg)

# aiocleverbot
An async python wrapper for cleverbot.
Does not require API KEY

![Downloads](https://pepy.tech/badge/aiocleverbot) ![PyPI](https://img.shields.io/pypi/v/aiocleverbot) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aiocleverbot) ![PyPI - License](https://img.shields.io/pypi/l/aiocleverbot)
## Installation
```pip
pip install aiocleverbot
```
## Usage
```python
from aiocleverbot import cleverbot

# Without context
response=await cleverbot("Hello")
print(response)

# With context
# Please note that context should include messages sent to Cleverbot as well as the responses
response=await cleverbot("Bad", ["hi", "How are you?"])
print(response)
