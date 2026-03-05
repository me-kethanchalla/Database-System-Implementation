# Database System Implementation 

This repository contains Python implementations of core database system mechanisms, developed as part of a Database System Implementation course[cite: 1]. It features a dynamic B+ Tree for indexing and a Buffer Management Simulator for optimizing disk I/O.

## Components

### 1. Dynamic B+ Tree
An in-memory B+ tree implementation that maintains balanced hierarchical indexing through automated restructuring.
* **Core Operations:** Supports dynamic key insertion and deletion, handling underflows, overflows, and node merging/borrowing.
* **Customizable Splitting:** Includes separate implementations for configurable node-splitting policies (left-biased vs. right-biased child distribution).
* **Configurable Order:** The degree of the tree (`d`) can be adjusted to simulate different node capacities.
* **Files:** `tree(left_more).ipynb`, `tree(right_more).ipynb`

### 2. LRU Buffer Management Simulator
A robust simulator that models how a database buffer pool manages memory frames and disk accesses.
* **Page Replacement Policy:** Implements the Least Recently Used (LRU) algorithm to determine the optimal page for eviction.
* **State Tracking:** Accurately monitors concurrent `pin` counts (active programs using a page) and `dirty` bits (modified pages).
* **I/O Operations:** Outputs exact page I/O instructions (`read`, `write`, `remove`), ensuring dirty pages are written back to disk before eviction.
* **File:** `lru.py`
