import os

from dotenv import load_dotenv, find_dotenv

load_dotenv()
# Only for testing. Not needed when the actual path is in .env or system environment variables
load_dotenv(find_dotenv(".env.test"), override=True)
words = set()
default_dictionary_path = os.getenv("DICTIONARY_PATH")

def load(dictionary):
    if not dictionary:
        try:
            with open(default_dictionary_path, "r") as file:
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