---
layout: post
title: Trie data structure
---

### Trie data structure

Trees have specific rules. Binary Tree holds only two child nodes. Binary Search Tree (BST) is a Binary Tree with special rules
where a left subtree is always smaller than the node's key and a right right subtree is always larger than the node's key.

Trie is a Tree, but completely different from a Binary Tree. First of all, unlike Binary Tree, a Trie can hold many child nodes.
Also, a root node of a Trie typically does not hold a key, but rather its role is a starting point for adding and searching words
(a.k.a prefix). 

#### Step 1. Here is a basic implementation of a Trie Node.

```py
class Node:
    """
    Trie Node implementation. Very basic.
    """
    def __init__(self, char: str = None):
        self.children = [] # Collection of Nodes
        self.char = char
        self.is_end_of_word = False

```

#### Step 2. A Trie data structure would hold a trie node as a root node.

```py
class Trie:
    """
    Trie structure that provides basic
    operations such as add and find.
    """
    def __init__(self):
        self.root = Node()
```
#### Step 3. Here is an implementation of adding a word to the Trie. This method should be placed inside the Trie class.

```py
    def add(self, word: str):
        """
        Add a word in the Trie structure
        """
        node = self.root
        for char in word:
            found = False
            for child in node.children:
                if child.char == char:
                    found = True
                    node = child
                    break
            if not found:
                new_node = Node(char)
                node.children.append(new_node)
                node = new_node
node.is_end_of_word = True 
```

### Step 4. Here is an implementation of a find method that determines whether a given word (prefix) exists in a Trie.
This method should be placed in the Trie class, too.

```py
    def find(self, word: str):
        """
        Determine if a given word exists in the Trie structure
        """
        node = self.root
        if not node.children:
            return False        
        for char in word:
            found = False
            for child in node.children:
                if child.char == char:
                    found = True
                    node = child
                    break
            if not found:
                return False
        return True
```

That's it. Here is the full code.

#### Full code with unit test
{% gist 8b22ddd3ccb42f10b71d7af75fad1830 %}
