from src.memorymanagement.overloaded_delete import Test

if __name__ == "__main__":
    test = Test()
    # This will invoke the overloaded __del__(self) implementation in Test class
    # Nonetheless, the __del__() is invoked automatically once the object is dereferenced
    del test
