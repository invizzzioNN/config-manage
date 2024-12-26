import os
import subprocess


class DependencyVisualizer:
    def __init__(self, repo_path, hash_value):
        self.repo_path = repo_path
        self.hash_value = hash_value

    def get_commit_messages(self):
        """Получить сообщения коммитов, где фигурирует файл с заданным хешем."""
        command = f"git log --pretty=format:'%h - %s' --all --grep={self.hash_value}"
        result = subprocess.run(command, cwd=self.repo_path, shell=True, text=True, capture_output=True)
        return result.stdout.splitlines() if result.returncode == 0 else []

    def build_dependency_graph(self):
        """Построить граф зависимостей в формате Mermaid."""
        commits = self.get_commit_messages()
        if not commits:
            return "graph TD; \n  No dependencies found."

        graph_lines = ["graph TD;"]
        for commit in commits:
            commit_hash, message = commit.split(" - ")
            graph_lines.append(f"  {commit_hash}(\"{message}\")")

        # Пример транзитивных зависимостей
        for i in range(len(commits) - 1):
            hash1 = commits[i].split(" - ")[0]
            hash2 = commits[i + 1].split(" - ")[0]
            graph_lines.append(f"  {hash1} --> {hash2}")

        return "\n".join(graph_lines)