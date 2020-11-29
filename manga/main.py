import message
from vizmedia import read_manga_html
import datetime

VIZ_MANGA_I_WANT = ['my-hero-academia', 'my-hero-academia-vigilantes']


if __name__ == "__main__":
    body = '\n \n'
    for manga in VIZ_MANGA_I_WANT:
        update = read_manga_html(manga)
        
        if update != '':
            body = body + '\n\n' + update
    

    message.send_message("+14693169332", "+17204632045", body)