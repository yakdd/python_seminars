import datetime

def log(message):
    with open('log.txt', 'a', encoding='utf-8') as log_file:
        who = message.from_user.first_name
        now = datetime.datetime.now()
        moment = now.strftime("%d-%m-%Y %H:%M:%S")
        content = message.text
        log_file.write(f'{who}:\t{moment}:\t{content}\n')
