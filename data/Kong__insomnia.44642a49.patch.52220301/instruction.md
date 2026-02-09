# Bug Report

### Describe the bug

I'm experiencing an issue with the delta patching functionality where text synchronization is producing incorrect results. When applying patch operations to a string, the output is missing characters and doesn't match what I expect.

### Reproduction

```js
const original = "Hello World";
const operations = [
  { type: 'COPY', start: 0, len: 5 },
  { type: 'INSERT', content: ' Beautiful' },
  { type: 'COPY', start: 5, len: 6 }
];

const result = patch(original, operations);
// Expected: "Hello Beautiful World"
// Actual: Gets corrupted/missing characters
```

When I try to sync content between clients, the patched text ends up malformed. It seems like characters are being skipped or insertions aren't happening when they should.

### Expected behavior

The patch function should correctly apply COPY and INSERT operations to reconstruct the target string. All characters from the original string should be preserved when copied, and insertions should always be applied.

### System Info
- Package: @insomnia/sync
- Version: latest

---
Repository: /testbed
