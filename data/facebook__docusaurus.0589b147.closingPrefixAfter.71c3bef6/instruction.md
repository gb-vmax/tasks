# Bug Report

### Describe the bug

I'm encountering an issue with directive container parsing where the token structure appears to be incorrect. When parsing closing fences for directive containers, the tokens are being generated in the wrong order, which breaks the expected AST structure.

### Reproduction

```js
// Parse a directive container with closing fence
const input = `
:::note
Content here
:::
`;

// The closing fence tokens are generated incorrectly
// Expected: directiveContainerFence wraps directiveContainerSequence
// Actual: directiveContainerSequence wraps directiveContainerFence
```

### Expected behavior

The token hierarchy should have `directiveContainerFence` as the parent token containing `directiveContainerSequence` as a child, matching the structure used for opening fences. This ensures consistent AST representation throughout the parsing process.

### Additional context

This affects any markdown content using directive containers with proper closing fences. The issue seems to be specific to the closing fence tokenization logic - the opening fence works correctly but the closing one has the tokens reversed.

---
Repository: /testbed
