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
![bg right:50% w:90%](../Lecture-Data-Structure-1/add_image/ch11/tree_concept.png)
- A generic tree is a data structure that consists of nodes connected by links. 
- Each node contains a value and a variable number of links to other nodes, from zero to some number k (the branching number of a k-ary tree, that is, the maximum number of links a node can have).

# Terminology of Tree (1/2)
- Root: no other node in the tree points to the root (0)
- Parent and Child node: a node P has a link to another node C, then P is called the **parent** of C, and C is a **child** of P. 0 is the parent node of two child nodes: 2 and 8
- Leaf: a node has no links to children (5, 1, 2, 3, 4, 7)
- Internal node: node has child nodes (2, 8, 6, 3)
- No loop in a tree: any path from the root to a leaf, you never see the same node twice
<div class="middle-grid">
    <img src="/add_image/ch11/tree_concept.png">
</div>

# Terminology of Tree (2/2)
- Ancestor: node N is an ancestor of node M if N is in the path between the root and M. 
- Descendant: a descendant of a node N is either one of the children of N or the descendant of one of the children of N. Node 8 is an ancestor of node 7.
- Sibling: All children of the same node are siblings.
- Subtree: a portion of the tree containing a node R and all the descendants of R.
- Height: the length of the longest path from the root to a leaf
<div class="middle-grid">
    <img src="/add_image/ch11/tree_terminology.png">
</div>

# Compare Linked List to Trees
![](/add_image/ch11/tree_compart_linked_list.png)

# Binary Tree
Binary trees are defined by restricting each node to a maximum of two children.
- In a binary tree, a node may have zero, one, or two child links. 
- There are left children and right children of a node, and thus its left and right subtrees
- The order of the children, however, isn’t always important for all binary trees.
 
<div class="middle-grid">
    <img src="/add_image/ch11/tree_binary_ternary.png">
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
    <img src="/add_image/ch11/tree_bst_order.png">
</div>

# Design to Find the Minimum and Maximum Elements in a Tree
- Get the maximum element, we start at the root and follow the links to the right children until we reach a node that has no right child. This node (which could be the root itself) stores the maximum value in the tree.
- Get the minimum element, we start at the root and follow the links to the left children until we reach a node that has no left child.
<div class="middle-grid">
    <img src="/add_image/ch11/tree_min_max.png">
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

# We do not allow a node’s value to be changed. no set_value function here.
# If you want to change the value of a node in the tree, you’ll have to create a new Node instance and set its children       
```

# Implement BST's Node (2/2)
```python
    def find_max_in_subtree(self):
        # Return the node with the largest value in the subtree rooted at the node, and its parent.
        parent = None
        node = self
        while node.right() is not None:
            parent = node
            node = node.?????() #right
        return node, parent
```
# Implement BST Helper Functions
```python
class BinarySearchTree:
    def __init__(self):
        self._root = None
    def __repr__(self):
        return f'BinarySearchTree({str(self)})'
    def __str__(self):
        return str(self._root)

    def __len__(self) -> bool:
        """Return the number of values stored in the tree."""
        # This version of the traversal algorithm uses an explicit stack, instead of recursion.
        stack = Stack()
        stack.push(self._root)
        size = 0
        while len(stack) > 0:
            node = stack.pop()
            if node is not None:
                size += 1
                stack.push(node.right())
                stack.push(node.left())
        return size
```

# Design BST Search
<div class="middle-grid">
    <img src="/add_image/ch11/tree_search_1.png">
    <img src="/add_image/ch11/tree_search_2.png">
</div>
The search method follows a single path, from the root to (possibly) a leaf, means that it will take no more steps than the height of the tree — it needs O(h) comparisons, where h is the height of the tree.

# Implement BST Search
```python
def _search(self, value):
        """Returns a tuple. 
           The first element is the node containing the target value, or None if not found.
           The second element is the parent of the node in the first position. 
           If the target wasn't found or if it was the root, the parent is set to None.
        """
        parent = None
        node = self._root
        while node is not None:
            node_val = node.value()
            if node_val == value:
                return node, parent
            elif value < node_val:
                parent = node
                node = node.left()
            else:
                parent = node
                node = node.right()
        return None, None
    def contains(self, value):
        return self._search(value)[0] is not None
```

# Design BST Insert
<div class="middle-grid">
    <img src="/add_image/ch11/tree_insert.png">
</div>

- In general, when we get to a node, we first check the value it stores to understand which branch we need to traverse and whether we need to go left or right. 
- Suppose we figure out that we need to go right. If the node has no right child, we have found the place where we have to add the new element. 
- All we have to do is create a new node and attach it as a right child of the current node. 

# Implement BST Insert
```python
def insert(self, value):       
        node = self._root
        if node is None: # Empty tree
            self._root = Node(value)
            return None
        
        while node is not None:
            if value <= node.value():
                if node.left() is ????: #None
                    node.set_????(Node(value)) #left
                    break
                else:
                    node = node.????()#left # We keep traversing the left branch 
            elif node.right() is ????: #None
                    node.set_?????(Node(value)) #right
                    break
            else:
                node = node.?????() #right # We keep traversing the right branch
```

# Design DST Delete (1/2)
 - Case 1: delete a leaf
 - Case 2: delete a node with only one child
 - Case 3: delete a node having two children

<div class="middle-grid">
    <img src="restricted/tree_delete_cases.png">
    <img src="restricted/tree_delete_leaf.png">
    <img src="restricted/tree_delete_one_child.png">
</div>

# Design DST Delete (2/2)
<div class="middle-grid">
    <img src="restricted/tree_delete_two_children_1.png">
    <img src="restricted/tree_delete_two_children_2.png">
    <img src="restricted/tree_delete_two_children_3.png">
</div>

# Implement BST Delete
```python
def delete(self, value):
        if self._root is None:
            raise ValueError('Delete on an empty tree')
        node, parent = self._search(value)
        if node is None:
            raise ValueError('Value not found')
        if node.left() is None or node.right() is None:  # The node has at most only one child
            if node.left() is None:
                maybe_child = node.right() 
            else:
                maybe_child = node.left()
            if parent is None:  # The node is the root
                self._root = maybe_child
            elif value <= parent.value():
                parent.set_left(maybe_child)
            else:
                parent.set_right(maybe_child)
        else: # The node N has two children.
            # Find and remove the node M with the largest value in the left subtree of N.
            max_node, max_node_parent = node.left().find_max_in_subtree()
            if max_node_parent is None: # M is the left child of N.
                new_node = Node(max_node.value(), None, node.right())
            else:
                new_node = Node(max_node.value(), node.left(), node.right())
                max_node_parent.set_right(max_node.left())
            # Then  replace the node to be deleted with a new node with M.value(), and the same subtrees as N.
            if parent is None:
                # The node is the root
                self._root = new_node
            elif value <= parent.value():
                parent.set_left(new_node)
            else:
                parent.set_right(new_node)
```

# Recap
- Trees are data structures consisting of nodes. Each node stores a value and a certain number of links to children. Each child is the root of a valid subtree.
- In binary trees, each node can have zero, one, or two children. Nodes without children are called leaves. The other nodes, called internal nodes, have one or two children.
- Links to children in a binary tree are usually labeled “left” and “right.” In some, but not all, binary trees, this distinction may have a meaning.
- In BST, for any node N, the left subtree of N can only contain values not greater than N’s, and the right subtree can only contain values greater than N’s. 
- BSTs are good for search — if the tree is balanced, search can be completed by comparing at most O(log(n)) elements.