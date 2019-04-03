from configparser import ConfigParser
import logging

conf = ConfigParser()
conf.read(conf)

try:
    _log = conf.get('General', 'log_file')
except Exception:
    logging.info('No log set! Will log in console only.')
    _log = None
finally:
    logging.info('Config loaded...')

logging.getLogger('').handlers = []
_debug = conf.getboolean('General', 'debug')

formatter = logging.Formatter('%(asctime)s %(name)-10s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s')
handler = logging.FileHandler(self._log)
handler.setFormatter(formatter)
fileLogger = logging.getLogger('')
fileLogger.addHandler(handler)
if _debug:
    fileLogger.setLevel(logging.DEBUG)
else:
    fileLogger.setLevel(logging.INFO)
