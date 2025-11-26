# initialize table
class HashTable:
    def __init__(self, size=10):
        self.size =size
        self.table=[[]for _ in range(size)]
        # hash function
    def _hash(self,key):
        hash_value= hash(key) #get a bigger number
        index = hash_value % self.size # fit it in our table
        return index
    #inserting data
    def insert(self, key,value):
        index=self._hash(key)# find where it should go
        for i, (k,v) in enumerate(self.table[index]):
            if k==key:
                self.table[index][i]= (key, value)
                return
        #key doesnt exist add it
        self.table[index].append((key,value))
    # getting data
    def get(self,key):
        index = self._hash(key)  # Calculate the index first!
        #search through the list at that index
        for k,v in self.table[index]:
            if k== key :
                return v
        raise KeyError("key not found ")

    #deleting data
    def delete(self, key):
        index = self._hash(key)
        #find and remove the item
        for i ,(k,v) in enumerate(self.table[index]):
            if k == key :
                self.table[index].pop(i)
                return v
        raise KeyError("key not found")


    # load factor and resize
    def _resize(self):
        old_table = self.table
        self.size *= 2  # Double the size
        self.table = [[] for _ in range(self.size)]

        # Rehash everything (move to new spots)
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

# simple example
# Create a phone book

print("=" * 60)
print("HASH TABLE DEMO - Phone Book Example")
print("=" * 60)

# STEP 1: Create a phone book with 5 buckets
print("\n[STEP 1] Creating hash table with 5 buckets")
phone_book = HashTable(5)
print(f"Initial table: {phone_book.table}")
print("Result: [[], [], [], [], []]  (5 empty buckets)")

# STEP 2: Add contacts
print("\n[STEP 2] Adding Alice's contact")
phone_book.insert("Alice", "555-0001")
print(f"After insert: {phone_book.table}")
print(f"Alice stored in bucket {phone_book._hash('Alice')}")

print("\n[STEP 3] Adding Bob's contact")
phone_book.insert("Bob", "555-0002")
print(f"After insert: {phone_book.table}")
print(f"Bob stored in bucket {phone_book._hash('Bob')}")

print("\n[STEP 4] Adding Charlie's contact")
phone_book.insert("Charlie", "555-0003")
print(f"After insert: {phone_book.table}")
print(f"Charlie stored in bucket {phone_book._hash('Charlie')}")

# STEP 3: Look up a number
print("\n[STEP 5] Looking up Alice's number")
alice_number = phone_book.get("Alice")
print(f"Alice's number: {alice_number}")
print(f"How it worked: Checked bucket {phone_book._hash('Alice')} and found the value")

# STEP 4: Update a number
print("\n[STEP 6] Updating Alice's number to 555-9999")
phone_book.insert("Alice", "555-9999")  # Same key, new value = update
print(f"After update: {phone_book.table}")
alice_new = phone_book.get("Alice")
print(f"Alice's new number: {alice_new}")

# STEP 5: Delete a contact
print("\n[STEP 7] Deleting Bob's contact")
deleted_value = phone_book.delete("Bob")
print(f"Deleted value: {deleted_value}")
print(f"After delete: {phone_book.table}")

# STEP 6: Try to get a deleted contact
print("\n[STEP 8] Trying to look up Bob (should fail)")
try:
    phone_book.get("Bob")
except KeyError as e:
    print(f"Error caught: {e}")
    print("This is expected - Bob was deleted!")

print("\n" + "=" * 60)
print("SUMMARY OF OPERATIONS")
print("=" * 60)
print("✓ insert(key, value) - Adds or updates a key-value pair")
print("✓ get(key) - Retrieves the value for a key")
print("✓ delete(key) - Removes a key-value pair")
print("✓ _hash(key) - Determines which bucket to use")
print("✓ _resize() - Doubles table size when needed")
print("=" * 60)