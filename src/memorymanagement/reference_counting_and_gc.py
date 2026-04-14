'''
Python manages memory automatically using two mechanisms together:

1. Reference counting (primary mechanism)
2. Garbage collection (for special cases like circular references)

Summary of memory management in Python:

Create object
      ↓
reference count = 1
      ↓
references added / removed
      ↓
if ref_count == 0
      ↓
object destroyed

Circular references are cleaned by garbage collector.
'''
import gc
import sys

if __name__ == "__main__":
    print()
    a = [1, 2, 3]       # Reference count = 1
    b = a       # Reference count = 2 (both a and b point to the same object)
    print(f"a reference count = {sys.getrefcount(a)}")       # This will print 3 (actual RC = 2) because a temporary reference is passed to getrefcount() function
    print(f"b reference count = {sys.getrefcount(b)}")       # This will print 3 (actual RC = 2) because a temporary reference is passed to getrefcount() function
    del a       # Now only 1 reference to the object remains, i.e., b
    # print(sys.getrefcount(a))       # Will give error since a has been deleted and doesn't exist in memory
    print(f"b actual reference count (post a's deletion) = {sys.getrefcount(b) - 1}")       # Actual reference count = 1, but sys.getrefcount(b) will return 2
    del b       # Reference count = 0 (both a and b references have been deleted)

    '''
    Reference counting fails when objects reference each other (Circular References).
    Python has a cyclic garbage collector to detect circular references.
    The GC periodically scans objects and removes unreachable cycles.
    
    Python's GC divides objects into generations.
    Generation 0 → new objects
    Generation 1
    Generation 2 → long-lived objects
    
    Idea:
    Most objects die young
    So Python checks young objects more frequently.
    
    To force GC, use - 
    gc.collect(generation=2)
    
    With no arguments, run a full collection. 
    The optional argument generation may be an integer specifying which generation to collect (from 0 to 2). 
    A ValueError is raised if the generation number is invalid. 
    The sum of collected objects and uncollectable objects is returned.
    The free lists maintained for a number of built-in types are cleared whenever a full collection 
    or collection of the highest generation (2) is run. 
    Not all items in some free lists may be freed due to the particular implementation, in particular float.
    
    The effect of calling gc.collect() while the interpreter is already performing a collection is undefined.
    '''

    list1 = [1,2,3]
    list2 = [4,5,6]
    # Appending both lists into one another will create a circular reference
    # making it not possible for reference counting mechanism to free up the memory,
    # since the reference count will never reach 0 even when the references are deleted.
    # This need to be handled by the Python's Garbage Collector.
    list1.append(list2)
    list2.append(list1)
    print(f"list1 reference count = {sys.getrefcount(list1)}")
    print(f"list2 reference count = {sys.getrefcount(list2)}")
    del list1
    print(f"list2 reference count (post deleting list1) = {sys.getrefcount(list2)}")

    print(f"Is GC enabled: {gc.isenabled()}")
    print(f"Current GC count = {gc.get_count()}")
    # gc.get_count() example output:
    # (320, 5, 1)
    #
    # Meaning:
    # objects in generation 0
    # objects in generation 1
    # objects in generation 2

    # gc.collect(generation=2) or simply gc.collect() scans all three generations (0, 1, and 2).
    # Since Generation 2 contains long-lived objects that have survived multiple previous cycles, this is the only way to reclaim memory from them.
    # gc.collect(1): Scans and reclaims unreachable objects in Generation 0 and Generation 1 only.
    gc.collect(generation=2)
    print(f"Current GC count post garbage collection trigger = {gc.get_count()}")
