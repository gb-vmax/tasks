# Bug Report

### Describe the bug

I'm experiencing an issue with MDX container flow rendering where the first child element in a container is being skipped during serialization. When converting MDX AST nodes with multiple children, only elements starting from the second child onwards are being processed correctly.

### Reproduction

```js
const container = {
  type: 'root',
  children: [
    { type: 'paragraph', children: [{ type: 'text', value: 'First paragraph' }] },
    { type: 'paragraph', children: [{ type: 'text', value: 'Second paragraph' }] },
    { type: 'paragraph', children: [{ type: 'text', value: 'Third paragraph' }] }
  ]
};

// After serialization, only 'Second paragraph' and 'Third paragraph' appear
// 'First paragraph' is missing from the output
```

### Expected behavior

All children in the container should be processed and included in the serialized output. The first child element should not be skipped.

### Additional context

This appears to affect any container with flow content (paragraphs, headings, lists, etc.). The issue seems to be related to how the index is being incremented when iterating through children. Also noticing that an extra newline separator is being added at the end where it shouldn't be.

---
Repository: /testbed
