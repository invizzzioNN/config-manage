class Parser:
    def parse(self, command_line):
        parts = command_line.strip().split()
        if not parts:
            return None, None
        command = parts[0]
        args = parts[1:]
        return command, args