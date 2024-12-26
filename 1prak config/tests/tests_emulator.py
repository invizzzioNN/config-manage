import unittest
from unittest.mock import MagicMock
from datetime import datetime
from src.commands.cd import CdCommand
from src.commands.ls import LsCommand
from src.commands.exit import ExitCommand
from src.commands.uniq import UniqCommand
from src.commands.uptime import UptimeCommand
from src.core.emulator import Emulator

class TestEmulator(unittest.TestCase):
    def setUp(self):
        # Создаем мок для эмулятора и его зависимостей
        self.emulator = MagicMock()
        self.emulator.vfs = MagicMock()
        self.emulator.logger = MagicMock()
        self.emulator.parser = MagicMock()
        self.emulator.start_time = datetime(2024, 12, 25, 0, 0, 0)
        
    def test_init_filesystem_success(self):
        # Проверяем успешную инициализацию файловой системы
        self.emulator.vfs.change_dir.return_value = '/new/path'
        self.emulator.init_filesystem()
        self.emulator.vfs.change_dir.assert_called()

    def test_run_script_success(self):
        # Проверяем успешное выполнение скрипта
        self.emulator.script_path = "test_script.sh"
        self.emulator.run_script()
        # Проводим проверки для выполнения команд из скрипта

    def test_run_script_failure(self):
        # Проверяем ошибку при отсутствии скрипта
        self.emulator.script_path = "nonexistent_script.sh"
        with self.assertRaises(SystemExit):  # Ожидаем завершение при ошибке
            self.emulator.run_script()

    def test_execute_command_success(self):
        # Проверяем успешное выполнение команды
        self.emulator.parser.parse.return_value = ("ls", [])
        self.emulator.execute_command("ls")
        self.emulator.commands["ls"].execute.assert_called_with([])

    def test_execute_command_invalid(self):
        # Проверяем выполнение несуществующей команды
        self.emulator.parser.parse.return_value = ("invalid_command", [])
        with self.assertRaises(KeyError):  # Ожидаем ошибку при неправильной команде
            self.emulator.execute_command("invalid_command")

class TestCdCommand(unittest.TestCase):
    def setUp(self):
        self.emulator = MagicMock()
        self.cd_command = CdCommand(self.emulator)

    def test_cd_success(self):
        # Настроим mock для успешной смены каталога
        self.emulator.vfs.change_dir.return_value = '/new/path'
        self.cd_command.execute(['/new/path'])
        self.emulator.vfs.change_dir.assert_called_with('/new/path')

    def test_cd_fail(self):
        # Настроим mock для несуществующего каталога
        self.emulator.vfs.change_dir.return_value = None
        with self.assertRaises(SystemExit):  # assuming SystemExit on failure
            self.cd_command.execute(['/nonexistent/path'])

class TestLsCommand(unittest.TestCase):
    def setUp(self):
        self.emulator = MagicMock()
        self.ls_command = LsCommand(self.emulator)

    def test_ls_success(self):
        # Настроим mock для успешного списка файлов
        self.emulator.vfs.list_dir.return_value = ['file1.txt', 'file2.txt']
        self.ls_command.execute(['.'])
        self.emulator.vfs.list_dir.assert_called_with('.')

    def test_ls_fail(self):
        # Настроим mock для несуществующего каталога
        self.emulator.vfs.list_dir.return_value = None
        with self.assertRaises(SystemExit):  # assuming SystemExit on failure
            self.ls_command.execute(['/nonexistent/path'])

class TestExitCommand(unittest.TestCase):
    def setUp(self):
        self.emulator = MagicMock()
        self.exit_command = ExitCommand(self.emulator)

    def test_exit(self):
        # Проверяем, что команда выхода работает
        self.exit_command.execute([])
        self.emulator.running = False

class TestUniqCommand(unittest.TestCase):
    def setUp(self):
        self.emulator = MagicMock()
        self.uniq_command = UniqCommand(self.emulator)

    def test_uniq_success(self):
        # Настроим mock для успешной фильтрации уникальных строк
        self.emulator.vfs.read_file.return_value = "line1\nline1\nline2\nline3"
        self.uniq_command.execute(["test.txt"])
        self.emulator.vfs.read_file.assert_called_with("test.txt")

    def test_uniq_fail(self):
        # Настроим mock для несуществующего файла
        self.emulator.vfs.read_file.return_value = None
        with self.assertRaises(SystemExit):  # assuming SystemExit on failure
            self.uniq_command.execute(["nonexistent.txt"])

class TestUptimeCommand(unittest.TestCase):
    def setUp(self):
        self.emulator = MagicMock()
        self.uptime_command = UptimeCommand(self.emulator)

    def test_uptime(self):
        # Настроим mock времени работы
        self.emulator.start_time = datetime(2024, 12, 25, 0, 0, 0)
        self.uptime_command.execute([])
        self.emulator.start_time = datetime.now()
        self.uptime_command.execute([])  # Проверка без ошибок

if __name__ == '__main__':
    unittest.main()
