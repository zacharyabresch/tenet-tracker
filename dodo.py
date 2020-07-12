def task_test():
    """Run tests"""
    return {"actions": ["pytest"]}


def task_coverage():
    """Generate & report test coverage"""
    return {"actions": ["coverage run --source src/ -m pytest", "coverage report"]}

