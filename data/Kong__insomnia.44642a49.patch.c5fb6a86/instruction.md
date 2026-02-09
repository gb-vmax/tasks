# Bug Report

### Describe the bug

I'm experiencing an issue with the sync delta patch functionality where text content is being truncated or corrupted during synchronization. When syncing larger documents or making multiple edits, the patched result doesn't match the expected output.

### Reproduction

```js
const original = "Hello World! This is a test document with some content.";
const operations = [
  { type: 'COPY', start: 0, len: 50 },
  { type: 'INSERT', content: ' Additional text.' },
  { type: 'COPY', start: 50, len: 5 }
];

const result = patch(original, operations);
// Result is truncated and missing characters
```

### Expected behavior

The patch function should correctly apply all operations and produce the full expected string without truncation or missing characters. All COPY operations should preserve the exact content from the original string.

### Additional context

This seems to happen when:
- Working with documents longer than a certain size
- Multiple COPY operations are involved
- The operations span across different parts of the original text

The synced content ends up being incomplete or has missing characters at the boundaries of COPY operations.

---
Repository: /testbed
