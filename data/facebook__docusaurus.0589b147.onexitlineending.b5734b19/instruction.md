# Bug Report

### Describe the bug

I'm experiencing an issue with line ending handling in markdown parsing. When a hard break is followed by a line ending, the position tracking seems to be off. Additionally, line endings are being inserted in places where they shouldn't be based on the context type.

### Reproduction

```js
const markdown = `
Some text\\
with a hard break
and continuation
`;

// Parse the markdown
const tree = remark.parse(markdown);

// The position of nodes after hard breaks appears incorrect
// Also seeing unexpected line ending nodes in contexts that shouldn't contain them
```

### Expected behavior

1. After a hard break, the position end should correctly point to the last child element
2. Line endings should only be added to contexts that can contain end-of-line characters (based on `canContainEols` configuration)

### Additional context

This affects markdown documents that use hard breaks (double spaces or backslash before newline) and may result in incorrect AST node positions or unexpected text nodes being created in the parse tree.

---
Repository: /testbed
