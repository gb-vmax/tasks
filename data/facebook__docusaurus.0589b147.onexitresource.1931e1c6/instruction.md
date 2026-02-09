# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with reference handling in markdown parsing. When processing markdown with references (like links or images), the reference data appears to be persisting incorrectly between different nodes, causing unexpected behavior in the parsed output.

### Reproduction

```js
// Parse markdown with multiple references
const markdown = `
[link1][ref1]
[link2][ref2]

[ref1]: https://example.com
[ref2]: https://example.org
`;

// After parsing, reference data from previous nodes
// seems to leak into subsequent nodes
```

The issue seems to occur when exiting resource nodes - the reference state isn't being cleaned up properly, which affects how subsequent references are processed.

### Expected behavior

Each reference should be processed independently without state from previous references affecting the current one. The reference data should be properly cleared when exiting a resource node.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
