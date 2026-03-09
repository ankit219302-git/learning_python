from dictionary import check, load

def spell_check(word):
    if check(word):
        print("The entered word is correctly spelled")
        return
    print("The entered word is incorrectly spelled")

if __name__ == "__main__":
    load(None)
    input_word = input("Please enter a word to check: ")
    spell_check(input_word)