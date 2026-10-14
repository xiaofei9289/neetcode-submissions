class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.reach_end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        present_node = self.root
        for ele in word:
            if ele not in present_node.children:
                present_node.children[ele] = TrieNode()
            present_node = present_node.children[ele]
        present_node.reach_end = True

    def search(self, word: str) -> bool:
        present_node = self.root
        for ele in word:
            if ele not in present_node.children:
                return False
            present_node = present_node.children[ele]
        return present_node.reach_end
        

    def startsWith(self, prefix: str) -> bool:
        present_node = self.root
        for ele in prefix:
            if ele not in present_node.children:
                return False
            present_node = present_node.children[ele]
        return True
        
        