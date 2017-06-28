from functools import wraps


import logging


def lazy_property(func):

    _name = '_' + func.__name__

    @property
    def wrapper(self, *args, **kwargs):
        if not hasattr(self, _name):
            setattr(self, _name, func(*args, **kwargs))

        return getattr(self, _name)

    return wrapper


def specific_people(name=None):
    """

    :param name:
    :return:
     name为None表示任何人可调用该组件功能
    """
    def decorator(func):
        @wraps(func)
        def wrapper(self, msg, extra, *args, **kwargs):
            if name is None:
                return func(self, msg, extra, *args, **kwargs)
            else:
                from_name = msg['ToUserName']
                content = msg['Content']
                if from_name != name:
                    logging.info('{}调用组件失败, 此组件只可被{}调用，调用语句为{}'.format(from_name, name, content))
                    return
                else:
                    return func(self, msg, extra, *args, **kwargs)

        return wrapper
    return decorator
