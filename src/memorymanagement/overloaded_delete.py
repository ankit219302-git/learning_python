class Test:
    def __del__(self):
        print(f"Test object with id '{id(self)}' deleted")
