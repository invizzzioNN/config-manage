import sys
import os
import zipfile
import csv
from datetime import datetime

from src.core.filesystem import VirtualFileSystem
from src.core.logger import Logger
from src.core.parser import Parser
from src.commands.cd import CdCommand
from src.commands.ls import LsCommand
from src.commands.exit import ExitCommand
from src.commands.uniq import UniqCommand
from src.commands.uptime import UptimeCommand

class Emulator:
    def __init__(self, username, vfs_path, log_path, script_path):
        self.username = username
        self.vfs_path = vfs_path
        self.log_path = log_path
        self.script_path = script_path
        self.running = True
        self.vfs = None
        self.logger = None
        self.parser = Parser()
        self.commands = {
            'cd': CdCommand(self),
            'ls': LsCommand(self),
            'exit': ExitCommand(self),
            'uniq': UniqCommand(self),
            'uptime': UptimeCommand(self),
        }
        self.start_time = datetime.now()


    def init_filesystem(self):
        if not os.path.exists(self.vfs_path):
            print(f"Error: Virtual file system archive not found at '{self.vfs_path}'")
            sys.exit(1)
        try:
             with zipfile.ZipFile(self.vfs_path, 'r') as zip_ref:
                 self.vfs = VirtualFileSystem(zip_ref)
        except zipfile.BadZipFile:
             print(f"Error: The file '{self.vfs_path}' is not a valid zip file.")
             sys.exit(1)

    def init_logger(self):
        self.logger = Logger(self.log_path)

    def run_script(self):
        if self.script_path:
            if not os.path.exists(self.script_path):
                print(f"Warning: Startup script not found at '{self.script_path}'")
                return
            try:
                with open(self.script_path, 'r') as f:
                    for line in f:
                        command = line.strip()
                        if command:
                            self.execute_command(command)
            except Exception as e:
                 print(f"Error reading or executing startup script: {e}")

    def run(self):
        self.init_filesystem()
        self.init_logger()
        self.run_script()

        while self.running:
            try:
                 command_line = input(f"{self.username}@{self.vfs.get_current_dir()}> ")
                 if command_line.strip():
                    self.execute_command(command_line)
            except EOFError:
                print("\nExiting emulator.")
                self.running = False
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        if self.logger:
           self.logger.close()
       
    def execute_command(self, command_line):
        try:
            command, args = self.parser.parse(command_line)
            if command in self.commands:
                self.commands[command].execute(args)
                self.logger.log(self.username, command_line)
            else:
                print(f"Command not found: {command}")
        except Exception as e:
            print(f"Error executing command: {e}")