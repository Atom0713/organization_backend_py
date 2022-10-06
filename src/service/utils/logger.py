import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    f"%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)
