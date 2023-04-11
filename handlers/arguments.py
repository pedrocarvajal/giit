import argparse


class Arguments:
    __arguments = argparse.ArgumentParser()

    def __init__(self):
        self.__configure()

    def __configure(self):
        self.__arguments.add_argument(
            '--envrionment',
            help='Configure and set the envrionment.',
            default=None
        )

    @property
    def arguments(self):
        return vars(self.__arguments.parse_args())
