def add_item(lst):
    lst.append(4)

'''
Identity is the object's unique identifier assigned by Python, 
which is mostly the same as its memory address.
Even though Python doesn't guarantee that the identity and memory address will always be the same,
in CPython the identity is actually the memory address converted to decimal.
'''
if __name__ == '__main__':
    print("---------a, b and c comparisons---------")
    a = [1,2,3]
    b = a       # Memory reference (identity) will be same as 'a'
    c = [1,2,3]     # Memory reference (identity) is different from 'a' as both are different objects in memory

    print(a == b)       # True - compares value (equality) which is same
    print(a is b)       # True - compares memory reference (identity) which is same
    print(a == c)       # True - compares value which is same
    print(a is c)       # False - compares memory reference which is different
    print(b == c)       # True - compares value which is same
    print(b is c)       # False - compares memory reference which is different

    '''
    This behavior depends on whether the object is mutable.

    --Mutable objects--
    Can change in place.
    
    list
    dict
    set
    
    Example:
    a = [1,2,3]
    b = a
    b.append(4)
    Both a and b change.
    
    
    --Immutable objects--
    Cannot change after creation.
    
    int
    float
    str
    tuple
    
    Example:
    a = 10
    b = a
    b = b + 1
    Memory becomes:
    10 ← a
    11 ← b
    Python creates a new object instead of modifying the old one. So,
    print(a)  # 10
    print(b)  # 11
    '''

    print("\n---------d and e comparisons---------")
    d = [1,2,3]
    e = d.copy()        # This creates a new object in memory instead of pointing to the same memory reference
    print(d is e)       # False - memory references are different
    print(d == e)       # True - value are same
    d.append(4)
    print(d == e)       # False - since memory references are different, values added to one will not reflect in another


    print("\n---------Function pass by reference---------")
    a = [1,2,3]
    add_item(a)
    print(a)        # Will print [1, 2, 3, 4] because the function receives a reference to the same list.


    print("\n---------Integer caching---------")
    f = 256
    g = 256
    print(f is g)       # True - Python caches integer value and assigns new variables the same memory address if value is same
    print(f"f's identity (memory address) = {id(f)}")      # id() returns the identity or memory address of an object.
    print(f"g's identity (memory address) = {id(g)}")


    print("\n---------String interning---------")
    '''
    String interning is a memory optimization technique where Python stores only one copy of identical immutable strings 
    and reuses it wherever needed.
    Instead of creating multiple identical string objects, Python reuses the same object in memory.
    '''
    str1 = "Hello World"
    str2 = "Hello World"
    print(str1 is str2)     # True - Python caches string value and assigns new variables the same memory address if value is same
