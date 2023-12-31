import re
from constants import *

def contains_deleted_or_omitted(message):
    keywords = ["omitted", "This message was deleted.", "You deleted this message"]
    for keyword in keywords:
        if keyword in message:
            return True
    return False

def rm_square_brackets(message):
    message = re.sub(r"\[.*?\]", "", message).strip()
    message = message.replace('"', "")
    message = message.replace('{', "")
    message = message.replace('}', "")
    return message

def convert_to_instruction(msg_obj):
    return f"""{SYS_PROMPT}

### INPUT: {msg_obj["INPUT"]}

### {BOT_NAME}: {msg_obj[BOT_NAME]}
"""
