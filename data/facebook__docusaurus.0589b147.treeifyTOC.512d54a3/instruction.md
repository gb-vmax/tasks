# Bug Report

### Describe the bug

The table of contents (TOC) tree structure is not being built correctly when the first heading in a document is not an H2. When a document starts with an H3 or deeper heading level, that heading is incorrectly treated as a root node instead of being nested under a virtual parent.

### Reproduction

```js
const flatTOC = [
  { level: 3, value: 'First heading (H3)', id: 'h3-1' },
  { level: 2, value: 'Second heading (H2)', id: 'h2-1' },
  { level: 3, value: 'Third heading (H3)', id: 'h3-2' },
];

const tree = treeifyTOC(flatTOC);
// Expected: All headings should be in a proper hierarchy
// Actual: The first H3 appears as a root node alongside the H2
```

### Expected behavior

When a document starts with a heading level deeper than H2 (like H3, H4, etc.), it should still be properly nested in the tree structure. The heading should not appear as a root node in the TOC tree.

For example, if a document has:
- H3 (level 3)
- H2 (level 2) 
- H3 (level 3)

The first H3 should be treated as having a virtual parent at level 2, not as a root node.

### System Info
- Docusaurus theme-common package
- Affects TOC rendering in documentation pages

---
Repository: /testbed
