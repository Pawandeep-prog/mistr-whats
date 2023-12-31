import re


def contains_deleted_or_omitted(message):
    keywords = ["omitted", "This message was deleted.", "You deleted this message"]
    for keyword in keywords:
        if keyword in message:
            return True
    return False


def rm_square_brackets(message):
    return re.sub(r"\[.*?\]", "", message).strip()
