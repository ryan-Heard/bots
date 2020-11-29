import message
from vizmedia import read_manga_html
import datetime
import os

VIZ_MANGA_I_WANT = ['my-hero-academia', 'my-hero-academia-vigilantes']
sender_num = os.environ['SENDER_NUM']
my_num = os.environ['MY_NUM']


if __name__ == "__main__":
    body = ''
    for manga in VIZ_MANGA_I_WANT:
        update = read_manga_html(manga)
        
        if update != '':
            body = body + '\n\n' + update
    
    if body != '':
        message.send_message(my_num, sender_num, body)