class LsCommand:
    def __init__(self, emulator):
        self.emulator = emulator

    def execute(self, args):
        path = args[0] if args else '.'
        items = self.emulator.vfs.list_dir(path)
        if items is None:
             print(f"ls: cannot access '{path}': No such file or directory")
        else:
            print('  '.join(items))