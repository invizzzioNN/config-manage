import toml
import sys
from dependency_visualizer import DependencyVisualizer

def main():
    # Загрузка конфигурации
    try:
        config = toml.load('config.toml')
    except Exception as e:
        print(f"Ошибка при загрузке конфигурации: {e}")
        sys.exit(1)

    visualizer = DependencyVisualizer(
        repo_path=config['repository']['path'],
        hash_value=config['repository']['hash_value']
    )

    # Построение графа зависимостей
    graph_code = visualizer.build_dependency_graph()

    # Вывод графа в консоль
    print(graph_code)

if __name__ == '__main__':
    main()