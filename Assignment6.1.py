 class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a contact name
    def insert(self, word):
        current = self.root
        for ch in word.lower():
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.is_end_of_word = True

    # Search for a complete contact name
    def search(self, word):
        current = self.root
        for ch in word.lower():
            if ch not in current.children:
                return False
            current = current.children[ch]
        return current.is_end_of_word

    # Check if any contact starts with the given prefix
    def starts_with(self, prefix):
        current = self.root
        for ch in prefix.lower():
            if ch not in current.children:
                return False
            current = current.children[ch]
        return True


# ----------- Example Test Case -----------

trie = Trie()

contacts = ["Anil", "Anitha", "Anirudh", "Bala", "Balaji"]

# Insert contacts
for contact in contacts:
    trie.insert(contact)

# Operations
print(f'Contact "Anil" found → {trie.search("Anil")}')
print(f'Contact "Anand" not found → {trie.search("Anand")}')
print(f'Prefix "Ani" exists → {trie.starts_with("Ani")}')
print(f'Prefix "Bal" exists → {trie.starts_with("Bal")}')
