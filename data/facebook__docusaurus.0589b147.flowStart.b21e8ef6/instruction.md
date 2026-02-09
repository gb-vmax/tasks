# Bug Report

### Describe the bug

I'm experiencing an issue with MDX document parsing where containers are being exited at the wrong time when processing flow content. When parsing documents with null code points, the exit order seems to be incorrect - containers are getting closed before consuming the code, which breaks the expected parsing flow.

### Reproduction

```js
// When parsing MDX content that ends with a null code point
const mdxContent = `
# Some heading
Some content
`;

// The parser should:
// 1. Close any active flow if present
// 2. Exit all containers
// 3. Consume the null code point

// But currently the order is different, causing parsing issues
```

### Expected behavior

When encountering a null code point in flow content:
1. Any active child flow should be closed
2. Containers should be properly exited (with count 0)
3. The null code point should be consumed

The order of these operations matters for maintaining proper parser state.

### Additional context

This appears to affect how the document structure is finalized when parsing completes. The container exit and code consumption sequence needs to happen in the correct order to maintain parsing integrity.

---
Repository: /testbed
