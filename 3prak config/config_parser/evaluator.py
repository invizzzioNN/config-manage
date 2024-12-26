def evaluate_expression(expr, constants):
    """Вычисление выражения внутри ^[ ]"""
    try:
        # Замена констант в выражении
        for key, value in constants.items():
            expr = expr.replace(key, str(value))
        # Выполнение выражения
        return eval(expr, {"__builtins__": None}, {"mod": lambda x, y: x % y})
    except Exception:
        raise ValueError(f"Ошибка в выражении: {expr}")