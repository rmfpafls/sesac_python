import glob

def load_file():
    files = glob.glob(r'C:\Users\user\Desktop\RNN_중간실습\names\*.txt') 
    assert len(files) == 18

    data = []
    languages = []

    for file in files:
        with open(file) as f:
            names = f.read().strip().split('\n')
        lang = file.split('\\')[-1].split('.')[0]

        if lang not in languages:
            languages.append(lang)

        for name in names:
            data.append([name, lang])

    return data, languages


