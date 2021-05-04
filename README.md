![cleverbotfreeapi](https://www.cleverbot.com/images/cleverbot254x114.jpg)

# aiocleverbot
An async python wrapper for cleverbot.
Does not require API KEY

![Downloads](https://pepy.tech/badge/cleverbotfreeapi) ![PyPI](https://img.shields.io/pypi/v/cleverbotfreeapi) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cleverbotfreeapi) ![PyPI - License](https://img.shields.io/pypi/l/cleverbotfreeapi)
## Installation
```pip
pip install aiocleverbot
```
## Usage
```python
from aiocleverbot import cleverbot

# Without context
response=await cleverbot("Hello.")
print(response)

# With context
# Please note that context should include messages sent to Cleverbot as well as the responses
response=await cleverbot("Bad.", ["hi.", "How are you?"])

