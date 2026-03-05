# Database System Implementation Internals

[cite_start]This repository contains Python implementations of core database system mechanisms, developed as part of a Database System Implementation course[cite: 1]. It features a dynamic B+ Tree for indexing and a Buffer Management Simulator for optimizing disk I/O.

## 🚀 Key Components

### 1. Dynamic B+ Tree
[cite_start]An in-memory B+ tree implementation that maintains balanced hierarchical indexing through automated restructuring[cite: 234].
* [cite_start]**Core Operations:** Supports dynamic key insertion and deletion, handling underflows, overflows, and node merging/borrowing[cite: 4, 236, 237].
* [cite_start]**Customizable Splitting:** Includes separate implementations for configurable node-splitting policies (left-biased vs. right-biased child distribution)[cite: 572, 573].
* [cite_start]**Configurable Order:** The degree of the tree (`d`) can be adjusted to simulate different node capacities[cite: 225, 552].
* **Files:** `tree(left_more).ipynb`, `tree(right_more).ipynb`

### 2. LRU Buffer Management Simulator
[cite_start]A robust simulator that models how a database buffer pool manages memory frames and disk accesses[cite: 80, 83].
* [cite_start]**Page Replacement Policy:** Implements the Least Recently Used (LRU) algorithm to determine the optimal page for eviction[cite: 125].
* [cite_start]**State Tracking:** Accurately monitors concurrent `pin` counts (active programs using a page) and `dirty` bits (modified pages)[cite: 108, 118].
* [cite_start]**I/O Operations:** Outputs exact page I/O instructions (`read`, `write`, `remove`), ensuring dirty pages are written back to disk before eviction[cite: 95, 96, 97, 98, 100].
* **File:** `lru.py`
