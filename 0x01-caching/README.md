# Caching

## Resources

- [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29)
- [Cache replacement policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_%28LIFO%29)
- [Cache replacement policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_%28LRU%29)
- [Cache replacement policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_%28MRU%29)
- [Cache replacement policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_%28LFU%29)

## More Info
**Parent class BaseCaching**
- All your classes must inherit from BaseCaching defined below:

```$ cat base_caching.py```


```
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```



## Tasks
+ 0. **Basic dictionary**

Create a class BasicCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
This caching system doesn’t have limit
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.

**Code Explanation**:

The BasicCache class is defined as a subclass of BaseCaching. It implements the put and get methods required by the parent class.

The put method receives a key and an item. It checks if either is None, in which case it returns without doing anything. Otherwise, it assigns the item value to the key in the cache_data dictionary.

The get method receives a key. If the key is None or not present in the cache_data dictionary, it returns None. Otherwise, it returns the value associated with the key in the dictionary.
     
+ 1. **FIFO caching**

Create a class FIFOCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the first item put in cache (FIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.

**Code Explanation**:
The FIFOCache class is defined as a subclass of BaseCaching. It implements the put and get methods required by the parent class.

The constructor of the FIFOCache class calls the parent constructor using the super() function and initializes a queue to keep track of the order of insertion.

The put method receives a key and an item. It checks if either is None, in which case it returns without doing anything. If the number of items in the cache_data dictionary is equal to or greater than the MAX_ITEMS constant defined in the parent class, it removes the first item that was put into the cache (i.e., the oldest item) using the FIFO algorithm. It prints a message indicating the key that was discarded. Then it assigns the item value to the key in the cache_data dictionary and adds the key to the end of the queue.

The get method receives a key. If the key is None or not present in the cache_data dictionary, it returns None. Otherwise, it returns the value associated with the key in the dictionary.

+ 2. **LIFO Caching**

Create a class LIFOCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the last item put in cache (LIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.

**Code Explanation**:
The LIFOCache class is defined as a subclass of BaseCaching. It implements the put and get methods required by the parent class.

The constructor of the LIFOCache class calls the parent constructor using the super() function and initializes a stack to keep track of the order of insertion.

The put method receives a key and an item. It checks if either is None, in which case it returns without doing anything. If the number of items in the cache_data dictionary is equal to or greater than the MAX_ITEMS constant defined in the parent class, it removes the last item that was put into the cache (i.e., the newest item) using the LIFO algorithm. It prints a message indicating the key that was discarded. Then it assigns the item value to the key in the cache_data dictionary and adds the key to the top of the stack.

The get method receives a key. If the key is None or not present in the cache_data dictionary, it returns None. Otherwise, it returns the value associated with the key in the dictionary.

+ 3. **LRU Caching**

Create a class LRUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the least recently used item (LRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.

**Code Explanation**:
The LRUCache class inherits from BaseCaching and uses an OrderedDict from the collections module to keep track of the order in which items were added or accessed. The OrderedDict will automatically move items to the end when they are accessed or added, allowing us to easily determine the least recently used item.

In the put method, we first check if the key or item is None, and return if they are. If the key already exists in the cache, we remove it and add it back in to update the order. If the cache is full, we remove the first (least recently used) item and print a message indicating which key was discarded. Finally, we add the new item to the end of the OrderedDict.

In the get method, we first check if the key is None or not in the cache, and return None if it is. We then remove the item from the OrderedDict and add it back in to update the order, and return the value.
     
+ 4. **MRU Caching**

Create a class MRUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the most recently used item (MRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.

**Code Explanation**:
The MRUCache class inherits from the BaseCaching class, overrides the put() and get() methods, and adds an access_list to keep track of the most recently used keys.

In the put() method, we first check if the key and item are not None. Then, we check if the key already exists in the cache and update it. If it does not exist, we check if the cache has reached its maximum capacity. If it has, we remove the most recently used key from the access_list, delete it from the cache, and print a discard message. We then append the new key to the access_list and add the new item to the cache.

In the get() method, we first check if the key is not None and exists in the cache. We then remove the key from the access_list and append it to the end of the list to mark it as the most recently used. We then return the item associated with the key in the cache.
     
+ 5. **LFU Caching**

Create a class LFUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the least frequency used item (LFU algorithm)
if you find more than 1 item to discard, you must use the LRU algorithm to discard only the least recently used
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.

**Code Explanation**:
In this implementation, LFUCache overrides the put and get methods of BaseCaching. It also introduces two new methods: update_lfu_keys and evict.

update_lfu_keys updates the frequency of accessed keys and maintains the list of LFU keys.

evict is called when the cache is full and a new item needs to be added. It discards the least frequency used item, and if there are multiple items with the same frequency, it uses the LRU algorithm to discard the least recently used one.

Note that the LFU algorithm implemented in this class is a simplified version that only considers the frequency of key accesses, and does not take into account the time of last access or any other factors that could affect the cache performance.