"""
212. 单词搜索 II

给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例:

输入:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]
说明:
你可以假设所有输入都由小写字母 a-z 组成。

提示:

你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？
如果你想学习如何实现一个基本的前缀树，请先查看这个问题：
实现Trie（前缀树）。https://leetcode-cn.com/problems/implement-trie-prefix-tree/description/
"""
# 与LC79一样, 但是python TestCase通过为34/36, 未通过, 需要 前缀树 优化


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board: return False
        self.h, self.w = len(board), len(board[0])
        ans = []
        for word in words:
            if self.exist(board, word):
                ans.append(word)
        return ans

    def exist(self, board, words):

        def search(depth, x, y):
            if x < 0 or y < 0 or x == self.w or y == self.h or words[depth] != board[y][x]:
                return False
            if depth == len(words) - 1:
                return True

            curr = board[y][x]
            board[y][x] = ""
            found = search(depth+1, x+1, y) \
                    or search(depth+1, x-1, y) \
                    or search(depth+1, x, y+1) \
                    or search(depth+1, x, y-1)
            board[y][x] = curr

            return found

        return any(search(0, i, j) for i in range(self.w) for j in range(self.h))

    def findWords_2(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        trie = Trie()
        node = trie.root
        for word in words:
            trie.insert(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs_trie(board, node, i, j, "", res)
        return res

    def dfs_trie(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return

        board[i][j] = "#"
        self.dfs_trie(board, node, i+1, j, path+tmp, res)
        self.dfs_trie(board, node, i-1, j, path+tmp, res)
        self.dfs_trie(board, node, i, j-1, path+tmp, res)
        self.dfs_trie(board, node, i, j+1, path+tmp, res)
        board[i][j] = tmp


import collections


class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord


Solution().findWords_2(
    [["o","a","a","n"],
     ["e","t","a","e"],
     ["i","h","k","r"],
     ["i","f","l","v"]], ["oath", "pea", "eat", "rain"])
