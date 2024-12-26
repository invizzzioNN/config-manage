class ExitCommand:
    def __init__(self, emulator):
        self.emulator = emulator

    def execute(self, args):
        self.emulator.running = False