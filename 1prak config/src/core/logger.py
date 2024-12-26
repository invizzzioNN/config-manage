import csv
import os
from datetime import datetime

class Logger:
    def __init__(self, log_path):
        self.log_path = log_path
        self.log_file = None
        self.writer = None
        self.start_new_log()
    
    def start_new_log(self):
         if os.path.exists(self.log_path):
              try:
                   os.remove(self.log_path)
              except OSError as e:
                   print(f"Error removing the log file: {e}")
                   return

         try:
            self.log_file = open(self.log_path, 'w', newline='', encoding='utf-8')
            self.writer = csv.writer(self.log_file)
            self.writer.writerow(['Timestamp', 'User', 'Command'])
         except Exception as e:
             print(f"Error creating or opening log file: {e}")

    def log(self, user, command):
       try:
           timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
           self.writer.writerow([timestamp, user, command])
       except Exception as e:
            print(f"Error writing log: {e}")

    def close(self):
        if self.log_file:
           try:
             self.log_file.close()
           except Exception as e:
               print(f"Error closing log file: {e}")