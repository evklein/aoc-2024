import os

days = []

# Dynamically load all .py files in this directory except __init__
for filename in sorted(
    os.listdir(os.path.dirname(__file__)),
    key=lambda f: int(f[3:-3]) if f.startswith('day') and f.endswith('.py') else 0
):
    if filename.endswith('.py') and filename != '__init__.py':
        module_name = filename[:-3]
        module_class = module_name.capitalize()
        exec(f'from .{module_name} import {module_class}')
        if module_name.startswith('day'):
            days.append(eval(module_class))
