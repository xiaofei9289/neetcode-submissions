class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        present_node = self.root
        for ele in word:
            if ele not in present_node.children:
                present_node.children[ele] = TrieNode()
            present_node = present_node.children[ele]
        present_node.end_of_word = True

    def search(self, word: str) -> bool:
        present_node = self.root
        for ele in word:
            if ele not in present_node.children:
                return False
            present_node = present_node.children[ele]
        return present_node.end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        present_node = self.root
        for ele in prefix:
            if ele not in present_node.children:
                return False
            present_node = present_node.children[ele]
        return True
        
        