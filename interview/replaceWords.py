class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        def searchforsubstring(elem: str, dictionary: List[str]):#function to search if elem  or any of its substring is present in dictionary
            l_index = 0
            r_index = len(elem)
            while r_index >= 0:#most important property - we check for the actual element to be present - ifnot we dont increment left, but decrement right - which ensures we get the smallest sub possible 
                if elem[l_index:r_index] in dictionary:
                    elem = elem[l_index:r_index]
                    r_index -= 1
                else:
                    r_index -= 1
            return elem
#rest of it is all basic common sense 
        slist = sentence.split(' ')
        print(slist)
        new_list = []
        for elem in slist:
            elem = searchforsubstring(elem, dictionary)
            new_list.append(elem)
            print(elem)
        new_string = ' '.join(new_list)
        print(new_string)
        return new_string
'''
simple to implement - could be in btwen easy and medium
minue ised comcepts - searching for susbtring in a list - sliding window with indices on both ends , 


LETS SEE AN OPTIMA;L SOLUTION - MINE CODE WAS WAY TIME CONSUMING BUT SUPER STORAGE EFFICIENT
AS EXPECTED A TRIE APPROACH WITH INSERTING INTO A 26 ROOTED TREE AND DO INSERT, SEARCH, TIS BASICALLY A AUTOFILL TREE BUT EXTRA DUNCTION TO FIND SMALLEST PREFIX - CAN STUDY IT UP EASILY
'''

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isEndOfWord = True

    def search(self, word):
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return curr.isEndOfWord

    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return True

    def findShortedPrefix(self, word):
        curr = self.root
        for i, c in enumerate(word):
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return word
            curr = curr.children[index]
            if curr.isEndOfWord:
                return word[:i + 1]
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        tokens = sentence.split()
        result = []
        for token in tokens:
            prefix = trie.findShortedPrefix(token)
            result.append(prefix)
        return ' '.join(result)