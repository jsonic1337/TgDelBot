from pyrogram import Client, filters

delall = "/delall"
del_count = "oh"
del_count_edit = "oh-"

app = Client(
    "my_account",
    api_id=123456,    # Fill in from the https://my.telegram.org/apps
    api_hash="" # Fill in from the https://my.telegram.org/apps
)

@app.on_message(filters.text & filters.outgoing)
def bot(client, message):
    chat_id = message.chat.id
    if message.text == delall:
        msgs_list = client.get_chat_history(chat_id)
        ids_list = [msg.id for msg in msgs_list if msg.from_user.is_self]
        client.delete_messages(chat_id=chat_id, message_ids=ids_list)

    elif message.text.lower().startswith(del_count) and not (message.text.lower().startswith(del_count_edit)):
        count = 2 if message.text.lower() == del_count else int(message.text[2:])+1
        msgs_list = client.get_chat_history(chat_id)
        ids_list = [msg.id for msg in msgs_list if msg.from_user.is_self][:count]
        client.delete_messages(chat_id=chat_id, message_ids=ids_list)

    elif message.text.lower().startswith(del_count_edit):
        count = 2 if message.text.lower() == del_count_edit else int(message.text[3:])+1
        msgs_list = client.get_chat_history(chat_id)
        ids_list = [msg.id for msg in msgs_list if msg.from_user.is_self][:count]
        for i in ids_list:
            client.edit_message_text(chat_id=chat_id, message_id=i, text="[DELETED]")
            print(i)
        client.delete_messages(chat_id=chat_id, message_ids=ids_list)

app.run()
