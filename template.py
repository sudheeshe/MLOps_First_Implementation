import os


directories = [

    os.path.join('data', 'raw'),
    os.path.join('data','processed'),
    'data_given',
    'notebooks',
    'saved_models',
    'src',
    'report'

]

try:
    for dir_ in directories:
        os.makedirs(dir_, exist_ok=True)
        with open(os.path.join(dir_, '.gitkeep'), 'w') as f:
            pass

except Exception as e:
    print(e)


file_ = [
    'dvc.yaml',
    'params.yaml',
    '.gitignore',
    os.path.join('src', '__init__.py'),
    os.path.join('src','get_data.py'),
    os.path.join('src','load_data.py'),
    os.path.join('src','split_data.py'),
    os.path.join('src','train_and_evaluate.py'),
    os.path.join('report', 'params.json'),
    os.path.join('report', 'scores.json')
]

try:
    for file in file_:
        with open(file, 'w') as f:
            pass

except Exception as e:
    print(e)