from src.memorymanagement.overloaded_delete import Test

if __name__ == "__main__":
    test = Test()
    del test        # This will invoke the overloaded __del__(self) implementation in Test class
