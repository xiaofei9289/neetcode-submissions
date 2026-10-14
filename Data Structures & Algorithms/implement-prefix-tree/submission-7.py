class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur_node = self.root
        for ele in word:
            if ele not in cur_node.children:
                cur_node.children[ele] = TrieNode()
            cur_node = cur_node.children[ele]
        cur_node.is_end = True


    def search(self, word: str) -> bool:
        cur_node = self.root
        for ele in word:
            if ele not in cur_node.children:
                return False
            cur_node = cur_node.children[ele]
        return cur_node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for ele in prefix:
            if ele not in cur_node.children:
                return False
            cur_node = cur_node.children[ele]
        return True

        
        