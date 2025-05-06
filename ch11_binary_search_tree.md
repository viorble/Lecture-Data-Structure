---
marp: true
theme: default
class: invert
size: 16:9
paginate: true
footer: 國立陽明交通大學 電子與光子學士學位學程
headingDivider: 1
style: |
  section::after {
    content: attr(data-marpit-pagination) '/' attr(data-marpit-pagination-total);
  }
  
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .columns img {
    width: 100%;
  }

  .middle-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1rem;
  }
  .middle-grid img {
    width: 100%;
  }

  .red-text {
    color: red;
  }
  
  .blue-text {
    color: lightskyblue;  
  }

  .small-text {
    font-size: 0.50rem;
  }
---
# Chapter 11: Binary Search Tree
![bg right:50% w:90%](../Lecture-Data-Structure/restricted/tree_concept.png)
- A generic tree is a composite data structure that consists of nodes connected by links. 
- Each node contains a value and a variable number of links to other nodes, from zero to some number k (the branching number of a k-ary tree, that is, the maximum number of links a node can have).

# Terminology of Tree (1/2)
- Root: no other node in the tree points to the root (0)
- Parent and Child node: a node P has a link to another node C, then P is called the **parent** of C, and C is a **child** of P. 0 is the parent node of two child nodes: 2 and 8
- Leaf: a node has no links to children (5, 1, 2, 3, 4, 7)
- Internal node: node has child nodes (2, 8, 6, 3)
- No loop in a tree: any path from the root to a leaf, you never see the same node twice
<div class="middle-grid">
    <img src="restricted/tree_concept.png">
</div>

# Terminology of Tree (2/2)
- Ancestor: node N is an ancestor of node M if N is in the path between the root and M. 
- Descendant: a descendant of a node N is either one of the children of N or the descendant of one of the children of N. Node 8 is an ancestor of node 7.
- Sibling: All children of the same node are siblings.
- Subtree: a portion of the tree containing a node R and all the descendants of R.
- Height: the length of the longest path from the root to a leaf
<div class="middle-grid">
    <img src="restricted/tree_terminology.png">
</div>

# Compare Linked List to Trees
![](restricted/tree_compart_linked_list.png)

# Binary Tree
Binary trees are defined by restricting each node to a maximum of two children.
- In a binary tree, a node may have zero, one, or two child links. 
- There are left children and right children of a node, and thus its left and right subtrees
- The order of the children, however, isn’t always important for all binary trees.
 
<div class="middle-grid">
    <img src="restricted/tree_binary_ternary.png">
</div>

# Binary Search Trees
A binary search tree (BST) has some properties
- It’s a tree
- It’s binary, so each node has (optionally) a left and a right child
- It’s used for searching
- BST is potentially as fast as binary search on a sorted array.
- Insertion and deletion on BST can be faster than sorted arrays
- BST need more memory and more complicated than sorted array   

# BST is Order Matters
In BST, for any node N that stores a value v, all nodes in the left subtree of N will have values less than or equal to v, and all nodes in the right subtree of N will have values greater than v

<div class="middle-grid">
    <img src="restricted/tree_bst_order.png">
</div>

# Implement BST's Node (1/2)
```python
class Node:
    def __init__(self, value, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right
    def __str__(self):
        left_str = str(self._left)
        right_str = str(self._right)
        return f"{self._value} ({left_str})({right_str})"
    def value(self):
        return self._value
    def left(self):
        return self._left
    def right(self):
        return self._right
    def set_left(self, node):
        self._left = node
    def set_right(self, node):
        self._right = node
```
# Implement BST's Node (1/2)
```python
    def find_min_in_subtree(self):
    # Return the node with the smallest value in the subtree rooted at the node, and its parent
        parent = None
        node = self
        while node.left() is not None:
            parent = node
            node = node.left()
        return node, parent

    def find_max_in_subtree(self):
        # Return the node with the largest value in the subtree rooted at the node, and its parent.
        parent = None
        node = self
        while node.right() is not None:
            parent = node
            node = node.right()
        return node, parent
```
# Implement BST

# Recap