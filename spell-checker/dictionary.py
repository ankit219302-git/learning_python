words = set()

def load(dictionary):
    if not dictionary:
        try:
            with open("/Users/ankit/PycharmProjects/learning-python/spell-checker/resources/dictionary", "r") as file:
                words.update(file.read().splitlines())
                if size() == 0:
                    raise Exception("The dictionary is empty!!")
                return True
        except Exception as e:
            print("Dictionary can't be loaded.", e)
            exit()
    try:
        with open(dictionary, "r") as file:
            words.update(file.read().splitlines())
            if size() == 0:
                raise Exception("The dictionary is empty!!")
            return True
    except Exception as e:
        print("Dictionary can't be loaded.", e)
        exit()

def check(word):
    if size() == 0:
        raise Exception("The dictionary is empty!!")
    return word.lower() in words

def size():
    return len(words)