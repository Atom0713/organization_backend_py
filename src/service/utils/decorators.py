from flask import jsonify
from .logger import logger
from jwt.exceptions import ExpiredSignatureError

CUSTOMERROR = []

def handle_response(func):
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
        except ExpiredSignatureError as e:
            logger.error(f"JWT has expired: {e}")
            raise e
        except Exception as e:
            logger.error(e)
            if type(e) in CUSTOMERROR:
                # TODO does message exist? USe custom global Exception
                raise e
            return {"error": "Something went wrong!"}, 400
        return jsonify(response)

    wrapper.__name__ = func.__name__
    return wrapper
