class UniqCommand:
    def __init__(self, emulator):
        self.emulator = emulator

    def execute(self, args):
      if not args:
          print("uniq: missing file argument")
          return
      file_path = args[0]
      content = self.emulator.vfs.read_file(file_path)

      if content is None:
          print(f"uniq: {file_path}: No such file or directory")
          return
      
      lines = content.splitlines()
      if not lines:
            return
      
      unique_lines = []
      last_line = None
      for line in lines:
         if line != last_line:
              unique_lines.append(line)
              last_line = line
      print("\n".join(unique_lines))