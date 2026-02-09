# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where empty lists are causing unexpected behavior. When I have a loose list (list items separated by blank lines) that contains no items, the output includes extra newline text nodes that shouldn't be there.

### Reproduction

```js
// When processing an empty loose list
const nodes = [];
const loose = true;

// The wrap function is called with empty nodes array
const result = wrap(nodes, loose);

// Expected: empty array []
// Actual: [{ type: "text", value: "\n" }, { type: "text", value: "\n" }]
```

The problem occurs specifically when:
1. A list is marked as "loose" (has blank lines between items)
2. The list has no actual items/nodes
3. The wrapping function still adds opening and closing newlines

### Expected behavior

When wrapping an empty array of nodes, the result should be an empty array regardless of the `loose` parameter. Empty lists shouldn't produce any text nodes.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

This seems like it might be related to how the loop iteration is handled when the array is empty. The opening newline gets added but there's nothing to iterate over, yet a closing newline is still being appended.

---
Repository: /testbed
