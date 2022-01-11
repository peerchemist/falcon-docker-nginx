from os import environ

if environ.get('APP_ENV') == 'docker':
    loglevel = environ.get('LOGLEVEL', 'info')

else:
    loglevel = "debug"
