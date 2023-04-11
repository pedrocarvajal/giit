from handlers.arguments import Arguments
from helpers.log import Log
from enums.commands import Commands


class Terminal(
    Log,
    Arguments,
):
    def __init__(self):
        super().__init__()
        self.__command_execution()

    def __command_execution(self):
        envrionment = self.arguments.get('envrionment', None)

        if envrionment:
            self.print(
                message=f"You are changing the environment to {envrionment}"
            )

        Commands.ENVRIONMENT(
            envrionment=envrionment
        )
