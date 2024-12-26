import argparse
from src.core.emulator import Emulator

def main():
    parser = argparse.ArgumentParser(description="Simple Shell Emulator")
    parser.add_argument("-u", "--username", default="user", help="Username for the prompt")
    parser.add_argument("-v", "--vfs_path", required=True, help="Path to the virtual file system zip archive")
    parser.add_argument("-l", "--log_path", default="emulator.log", help="Path to the log file")
    parser.add_argument("-s", "--script_path", default=None, help="Path to the startup script")

    args = parser.parse_args()
    
    emulator = Emulator(args.username, args.vfs_path, args.log_path, args.script_path)
    emulator.run()

if __name__ == "__main__":
    main()