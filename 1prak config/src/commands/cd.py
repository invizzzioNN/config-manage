class CdCommand:
    def __init__(self, emulator):
        self.emulator = emulator

    def execute(self, args):
        if not args:
            print("cd: missing argument")
            return
        path = args[0]
        new_dir = self.emulator.vfs.change_dir(path)
        if new_dir is None:
            print(f"cd: '{path}': No such file or directory")