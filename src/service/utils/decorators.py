from .logger import logger


def handle_response(func):
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
        except Exception as e:
            logger.error(e)
            # TODO does message exist? USe custom global Exception
            return {"error": "Something went wrong!"}, 400
        return {"status": "ok", "data": response}

    wrapper.__name__ = func.__name__
    return wrapper
