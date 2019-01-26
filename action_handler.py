import input_handlers
from config import config


action = input_handlers.handle_keys(config.KEY)
move = action.get('move')
exit = action.get('exit')
fullscreen = action.get('fullscreen')



