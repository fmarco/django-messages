from django.conf import settings


class AppSettings(object):

    def __init__(self, prefix):
        self.prefix = prefix

    def _setting(self, name, dflt):
        from django.conf import settings
        return getattr(settings, self.prefix + name, dflt)

    @property
    def MESSAGE_MODEL(self):
        """
        Subject-line prefix to use for Message model setup
        """
        return self._setting("MESSAGE_MODEL", "chat.Message")

    @property
    def SAVE_ON_DB(self):
        """
        Save the message sent on the db
        """
        return self._setting('SAVE_ON_DB', True)

    @property
    def ROOM_MAX_LENGTH(self):
        """
        Room name max length
        """
        return self._setting('ROOM_MAX_LENGTH', 50)

    @property
    def CHECK_AUTH(self):
        """
        Check if user are authenticated
        """
        return self._setting('CHECK_AUTH', True)


app_settings = AppSettings('MESSAGES_')
