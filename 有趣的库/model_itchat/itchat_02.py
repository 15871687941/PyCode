import itchat


@itchat.msg_register(itchat.content.TEXT, isFriendChat=True, isGroupChat=True, isMpChat=True)
def print_content(msg):
    nickname = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    print(nickname + ":" + msg['Text'])
    return msg["Text"]


itchat.auto_login(hotReload=True)
print(itchat.get_friends(update=True))
itchat.run()
