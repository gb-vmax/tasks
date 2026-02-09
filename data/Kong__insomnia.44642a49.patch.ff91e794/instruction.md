# Bug Report

### Describe the bug
The sync delta patching system is producing incorrect results when applying operations to strings. Text is getting corrupted during the patch process, with characters missing or appearing in the wrong order.

### Reproduction
```js
const original = "hello world";
const operations = [
  { type: 'COPY', start: 0, len: 5 },
  { type: 'INSERT', content: ' beautiful' },
  { type: 'COPY', start: 5, len: 6 }
];

const result = patch(original, operations);
// Expected: "hello beautiful world"
// Actual: Result is malformed with missing/misplaced characters
```

### Expected behavior
The patch function should correctly apply COPY and INSERT operations in sequence to reconstruct the modified string. COPY operations should extract the exact substring specified by start position and length, and INSERT operations should add new content at the current position in the result.

### Additional context
This appears to affect text synchronization features. When syncing changes between clients, the resulting text doesn't match what was intended, leading to data corruption in synchronized documents.

---
Repository: /testbed
