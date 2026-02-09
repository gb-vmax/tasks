# Bug Report

### Describe the bug

I'm experiencing an issue with line ending handling in markdown parsing. When processing hard breaks in markdown content, the position tracking seems to be off - it's not pointing to the correct element in the children array.

### Reproduction

```js
const markdown = `
Some text with\\
a hard break
`;

const result = remark().parse(markdown);
// The position.end for the text before the hard break is incorrect
```

When parsing markdown with hard breaks (two spaces or backslash followed by newline), the position information for nodes seems to reference the wrong child element. This causes the end position to be set on an incorrect node in the AST.

### Expected behavior

The position tracking should correctly identify and update the last text node before a hard break. The `position.end` should be set on the actual tail element that precedes the line ending, not on a different element in the children array.

### Additional context

This appears to affect how line endings are processed after hard breaks. The logic for determining when to add data nodes for line endings also seems inverted - it's adding them when it shouldn't and vice versa.

---
Repository: /testbed
