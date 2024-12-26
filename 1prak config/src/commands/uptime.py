from datetime import datetime

class UptimeCommand:
    def __init__(self, emulator):
        self.emulator = emulator

    def execute(self, args):
      start_time = self.emulator.start_time
      current_time = datetime.now()
      uptime = current_time - start_time
      total_seconds = int(uptime.total_seconds())

      days = total_seconds // (60 * 60 * 24)
      hours = (total_seconds % (60 * 60 * 24)) // (60 * 60)
      minutes = (total_seconds % (60 * 60)) // 60
      seconds = total_seconds % 60

      print(f"Uptime: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")