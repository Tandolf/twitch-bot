from commands.base_command import BaseCommand

class TwitchPing(BaseCommand):
    def __init__(self, command, commandType, channel=None):
        super().__init__(command, commandType, channel)

    def is_match(self, response):
        if(response.startswith(self.command)):
            return True
        return False

    def execute(self, command):
        print("\U0001F3BE Responding to PING")
        return self.commandType + " :tmi.twitch.tv"