# Bug Report

### Describe the bug

The table of contents (TOC) tree structure is not being built correctly when there are headings at different levels. The parent-child relationships between TOC items appear to be incorrect, causing the hierarchy to be malformed.

### Reproduction

```js
const flatTOC = [
  { level: 2, value: 'Heading 2', id: 'h2' },
  { level: 3, value: 'Heading 3', id: 'h3' },
  { level: 4, value: 'Heading 4', id: 'h4' },
  { level: 2, value: 'Another H2', id: 'h2-2' }
];

const tree = treeifyTOC(flatTOC);
// The hierarchy doesn't match the heading levels
```

### Expected behavior

The TOC should properly nest headings based on their levels. For example:
- H2 items should be at the root level
- H3 items should be children of the preceding H2
- H4 items should be children of the preceding H3
- And so on...

Currently the parent indices seem to be calculated incorrectly, which breaks the nesting structure.

### System Info
- Package: @docusaurus/theme-common
- Using the `treeifyTOC` utility function

---
Repository: /testbed
