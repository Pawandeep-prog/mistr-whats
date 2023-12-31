import glob
from utils.preprocess_utils import *
import json
from constants import *
from utils.logger import *
import sys


if BOT_NAME == "":
    logger.info("Please set up BOT_NAME in the constants.py ---\nMake sure BOT_NAME is equal to one in the chats/*.txt same as you whatsapp user name")
    sys.exit(1)

chat_paths = glob.glob("./chats/*.txt")
logger.info(f"Reading chats from {chat_paths}")

## main object of conatining all chats
json_list = []

## reading chat file
for file_ in chat_paths:
    logger.info(f"Cleaning .... {file_}")
    chats = open(file_, "r").read().split("\n")[1:]

    ## first chat for setting prev_user = curr_user
    init = True
    prev_user = ""
    msg_buffer = ""
    ## contains cleaned final chat
    chats_clean = []

    ## iterate in chats
    for idx, txt in enumerate(chats):
        ## remove square brackets i.e. timestamp
        txt = rm_square_brackets(txt)
        ## message is deleted/ media message
        if contains_deleted_or_omitted(txt):
            continue

        ## split to get username and message separate
        split = txt.split(":")
        ## message from same user
        if len(split) == 1:
            msg_buffer += " " + txt
            continue

        user_name = split[0].strip()

        if init:
            init = False
            prev_user = user_name

        if user_name != prev_user:
            prefix = BOT_NAME + ":" if prev_user == BOT_NAME else "INPUT:"

            chats_clean.append(prefix + msg_buffer.strip())
            msg_buffer = ""

        prev_user = user_name
        msg_buffer += " " + split[-1].strip()

    for idx in range(0, len(chats_clean), 2):
        user1, msg1 = chats_clean[idx].split(":")
        user2, msg2 = chats_clean[idx + 1].split(":")
        json_list.append({user1: msg1, user2: msg2})

with open("./chats/clean_chats.json", "w") as f:
    f.write(json.dumps(json_list))
