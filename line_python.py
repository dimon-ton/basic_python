from email import message
from songline import Sendline

token = '--line-token--'

messenger = Sendline(token)

msg = 'Hello word chang'

ima_url ='https://i.pinimg.com/originals/e6/24/91/e62491454c2d44748e462ae6a2e2c2a9.jpg'


messenger.sendtext(msg + '\n' + messenger.sendimage(ima_url))