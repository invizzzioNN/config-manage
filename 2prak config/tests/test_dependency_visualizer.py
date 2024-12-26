import unittest
from unittest.mock import patch, MagicMock
from dependency_visualizer import DependencyVisualizer

class TestDependencyVisualizer(unittest.TestCase):
    @patch('subprocess.run')