"""
Python gives us powerful introspection tools:

- gc.get_objects()
- gc.get_count()
- gc.get_referrers()
- gc.get_referents()
- gc.garbage
- tracemalloc
These allow us to inspect the runtime memory graph of our program.

CPython actually maintains a linked list of all objects tracked by the garbage collector.
That’s why gc.get_objects() can list them.
But not every object is tracked.
For example:
- small integers
- simple strings
- tuples without references
are usually not tracked by GC because they cannot form cycles.
"""
import gc
import tracemalloc
from gc import DEBUG_SAVEALL

if __name__ == "__main__":
    # gc.get_objects() returns a list of objects tracked by the collector (excluding the list returned by get_objects() function)
    print(f"\nCurrent total objects in GC: {len(gc.get_objects())}")
    print(f"Current GC threshold: {gc.get_threshold()}")
    # gc.get_count() sample output:
    # (320, 5, 1)
    #
    # Meaning:
    # The tuple format is (count0, count1, count2):
    # count0 (Generation 0): This is typically the number of object allocations minus the number of deallocations
    #                        since the last generation 0 collection.
    # count1 (Generation 1): The number of times generation 0 has been collected since the last generation 1 collection.
    # count2 (Generation 2): The number of times generation 1 has been collected since the last generation 2 (full) collection.

    # Automatic garbage collection is triggered when these counts exceed the thresholds defined in the Python Garbage Collector interface.
    # We can view these thresholds using gc.get_threshold() and modify them with gc.set_threshold()

    # It is a common misconception that the numbers in gc.get_count() represent the total number of objects in each generation.
    # Instead, they track progress toward the next collection.
    # To find the actual number of objects currently tracked by the collector, we should use len(gc.get_objects())
    print(f"Current GC count (should be less than GC threshold): {gc.get_count()}")

    print("\n---------- Inspecting objects of a specific type ----------")
    # This is useful when debugging memory leaks where lists or other data structures keep growing
    list_objs = [obj for obj in gc.get_objects() if isinstance(obj, list)]
    print(f"Number of list objects in memory: {len(list_objs)}")
    int_objs = [obj for obj in gc.get_objects() if isinstance(obj, int)]
    print(f"Number of integer objects in memory: {len(int_objs)}")

    print("\n---------- Finding what references an object ----------")
    test_list = [1, 2, 3]
    test_list_temp:list = [test_list]       # :list is an example of 'type hint' - a way to explicitly define type

    print("1. Using 'test_list_temp:list = [test_list]' - ")
    # The output of below 2 statements will be -
    # Number of objects that directly refer to test_list: 2 (why not 1 - test_list_temp ?)
    # Number of objects that directly refer to test_list_temp: 1 (why not 0 ?)
    #
    # 1. Why test_list has 2 referrers -
    #    When we call gc.get_referrers(test_list), the following two objects are pointing to it:
    #    - test_list_temp: This is the reference we explicitly created ([test_list]).
    #    - The Local Namespace (locals()): Since we are running this in a script (under if __name__ == "__main__":),
    #      the variable name test_list itself is a key in the local symbol table dictionary.
    #      That dictionary holds a reference to the list object.
    # 2. Why test_list_temp has 1 referrer -
    #    Even though we haven't put test_list_temp inside another list or object, it still has one referrer:
    #    - The Local Namespace (locals()): Just like the previous example,
    #      the local symbol table dictionary holds the reference to the object so we can access it via the name test_list_temp.
    #
    # gc.get_referrers() shows all references, including:
    # - Local variables in the scope (frame objects).
    # - Global variables.
    # - Container objects (lists, dicts) holding the item.
    print(f"Number of objects that directly refer to test_list: {len(gc.get_referrers(test_list))}")
    print(f"Number of objects that directly refer to test_list_temp: {len(gc.get_referrers(test_list_temp))}")

    print(f"\nLocals Dictionary - {locals()}")

    test_list = [1, 2, 3]
    test_list_temp: list = test_list

    print("\n2. Using 'test_list_temp:list = test_list' -")
    # The output of below 2 statements will be -
    # Number of objects that directly refer to test_list: 1 (why not 2 ?)
    # Number of objects that directly refer to test_list_temp: 1
    #
    # 1. Both names point to the exact same object -
    #    There is only one list object in memory. test_list and test_list_temp are just two different labels for that same single object.
    # 2. Why the count is 1 (and not 2) -
    #    When we call gc.get_referrers(), we are asking: "What objects (like lists, dicts, or classes) point to this memory address?"
    #    - In Python, the local variables of a script are stored in a single dictionary (the locals() dictionary).
    #    - Even though we have two variable names (test_list and test_list_temp), they both live inside that one dictionary.
    #    - Therefore, the gc only sees one object (the locals dict) referring to our list.
    print(f"Number of objects that directly refer to test_list: {len(gc.get_referrers(test_list))}")
    print(f"Number of objects that directly refer to test_list_temp: {len(gc.get_referrers(test_list_temp))}")

    print("\n---------- Finding what an object references ----------")
    test_list_referent = [1, 2, 3]
    test_list_referent_temp: list = [test_list_referent]

    # The output of below 2 statements will be -
    # Number of objects that are directly referred to by test_list_referent: 3
    # Number of objects that are directly referred to by test_list_referent_temp: 1
    #
    # 1. test_list_referent (Length 3)
    #    Definition: test_list_referent = [1, 2, 3]
    #    Referents: The list object test_list_referent directly holds references to the integer objects: 1, 2, and 3.
    #    Output: 3 (because 1, 2, and 3 are in the list).
    # 2. test_list_referent_temp (Length 1)
    #    Definition: test_list_referent_temp: list = [test_list_referent]
    #    Referents: The list test_list_referent_temp holds exactly one object inside it:
    #    the list test_list_referent (which is [1, 2, 3]). It does not directly hold the integers 1, 2, 3 itself.
    #    Output: 1 (because only the container test_list_referent is inside).
    print(f"Number of objects that are directly referred to by test_list_referent: {len(gc.get_referents(test_list_referent))}")
    print(f"Number of objects that are directly referred to by test_list_referent_temp: {len(gc.get_referents(test_list_referent_temp))}")

    print("\n---------- Detecting Uncollectable Objects ----------")
    # In Python, gc.garbage is a list provided by the gc module that contains objects
    # the collector found to be unreachable but could not free.
    #
    # Uncollectable Objects: Historically, this list was primarily used to store objects involved in a circular reference
    #                        where at least one object had a __del__() (finalizer) method.
    #                        Because Python could not safely determine the order in which to run these finalizers,
    #                        it would move them to gc.garbage instead of deleting them.
    # Modern Python Behavior: Since Python 3.4 (via PEP 442), the garbage collector can now safely collect cycles
    #                         even if they contain __del__() methods. Consequently, gc.garbage is typically empty in modern Python
    #                         unless specific debugging flags are enabled.
    # Debugging Tool: We can force objects into this list for inspection by setting the gc.DEBUG_SAVEALL flag.
    #                 When this flag is active, all unreachable objects are appended to gc.garbage rather than being freed,
    #                 which is useful for tracking down memory leaks.
    #
    # Manual Cleanup: If we use DEBUG_SAVEALL, we must manually clear gc.garbage to actually free the memory,
    #                 as the list itself holds a reference to those objects.
    #                 We can do this with del gc.garbage[:]

    # DEBUG_STATS - Print statistics during collection.
    # DEBUG_COLLECTABLE - Print collectable objects found.
    # DEBUG_UNCOLLECTABLE - Print unreachable but uncollectable objects found.
    # DEBUG_SAVEALL - Save objects to gc.garbage rather than freeing them.
    # DEBUG_LEAK - This is a superset flag designed for debugging leaking programs.
    #              It is a bitwise combination of three other flags: DEBUG_COLLECTABLE | DEBUG_UNCOLLECTABLE | DEBUG_SAVEALL
    gc.set_debug(DEBUG_SAVEALL)         # DEBUG_LEAK is better for debugging memory leaks
    gc.collect()        # gc.garbage list is populated once collection occurs, else list will be empty
    print(len(gc.garbage))
    # 'del gc.garbage[:]' clears the contents of the list and is used for freeing memory in gc.garbage.
    # DO NOT use 'del gc.garbage' as it will try to delete the reference to the list itself which is usually incorrect.
    del gc.garbage[:]

    print("\n---------- Memory Leak Example ----------")
    initial_obj_count = len(gc.get_objects())
    print(f'Number of new objects prior to the "problematic" code execution: {initial_obj_count}')
    ########## SOME CODE WHERE LEAK MIGHT OCCUR ##########
    for i in range(1000):
        # The below statement creates a dynamic list type object with different variable name for each iteration of the for loop.
        exec(f"obj_list_{i} = [{i}]")
    ######################################################
    new_gc_eligible_objs_created = len(gc.get_objects()) - initial_obj_count
    print(f'Number of new objects (tracked by GC) created in the "problematic" code: {new_gc_eligible_objs_created}')

    print("\n---------- Memory Debugging With 'tracemalloc' ----------")
    tracemalloc.start()
    test_list_tracemalloc = [i for i in range(100000)]
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current tracemalloc memory usage: {current} bytes")
    print(f"Peak tracemalloc memory usage: {peak} bytes")
    tracemalloc.stop()
