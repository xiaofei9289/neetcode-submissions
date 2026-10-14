class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_node = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur_node = self.root
        for ele in word:
            if ele not in cur_node.children:
                cur_node.children[ele] = TrieNode()
            cur_node = cur_node.children[ele]
        cur_node.end_of_node = True
        

    def search(self, word: str) -> bool:
        def backtracking(start_index, node):
            if start_index == len(word):
                return node.end_of_node
            char = word[start_index]
            if char != ".":
                if char not in node.children:
                    return False
                return backtracking(start_index+1,node.children[char])
            else:
                for child in node.children.values():
                    if backtracking(start_index+1,child):
                        return True
                return False
        return backtracking(0,self.root)
        
