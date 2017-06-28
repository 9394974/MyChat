class BaseComponent(object):

    def parse_commands(self, msg, extra, *args, **kwargs):
        raise NotImplementedError()
