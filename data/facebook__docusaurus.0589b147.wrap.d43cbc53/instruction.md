# Bug Report

### Describe the bug

I'm experiencing an issue with markdown rendering where the last element in a list or block appears to be missing from the output. It seems like nodes at the end of arrays aren't being processed correctly.

### Reproduction

When processing markdown with multiple items, the final item doesn't appear in the rendered output:

```js
const nodes = [
  { type: 'paragraph', children: [...] },
  { type: 'paragraph', children: [...] },
  { type: 'paragraph', children: [...] }
]

// After processing, only 2 items appear in the result
// The third/last paragraph is missing
```

This affects any content where multiple nodes need to be wrapped - the last one just disappears from the final output.

### Expected behavior

All nodes should be included in the wrapped result, including the last element in the array. Every paragraph or list item should appear in the rendered markdown.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

---
Repository: /testbed
