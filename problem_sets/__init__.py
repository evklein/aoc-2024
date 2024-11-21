import os

days = []

# Dynamically load all .py files in this directory except __init__.py
for filename in os.listdir(os.path.dirname(__file__)):
    if filename.endswith('.py') and filename != '__init__.py':
        module_name = filename[:-3] 
        exec(f'from .{module_name} import {module_name.capitalize()}')
        if module_name.startswith('day'):
            days.append(eval(module_name.capitalize()))