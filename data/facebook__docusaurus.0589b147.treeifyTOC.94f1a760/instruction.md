# Bug Report

### Describe the bug

The table of contents (TOC) tree structure is not being built correctly when headings have mixed levels. Parent-child relationships between heading levels appear to be incorrectly assigned, causing the TOC hierarchy to break.

### Reproduction

```js
const tocItems = [
  { level: 2, value: 'Heading 2' },
  { level: 3, value: 'Heading 3' },
  { level: 4, value: 'Heading 4' },
  { level: 2, value: 'Another H2' }
];

const tree = treeifyTOC(tocItems);
// The hierarchy is incorrect - H3 and H4 are not properly nested under H2
```

When processing headings with different levels (H2, H3, H4), the parent index calculation seems off. For example, an H4 heading that should be nested under an H3 (which is under H2) doesn't get the correct parent assignment.

### Expected behavior

The TOC tree should correctly reflect the heading hierarchy:
- H2 headings should be root nodes
- H3 headings should be children of the preceding H2
- H4 headings should be children of the preceding H3
- And so on for deeper nesting levels

The parent-child relationships should be properly maintained regardless of which heading levels are used in the document.

---
Repository: /testbed
