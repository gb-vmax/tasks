# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where certain character codes aren't being handled correctly. It seems like the tokenizer is not properly processing constructs when specific code points are encountered.

### Reproduction

```js
// When parsing MDX content with special characters
const mdxContent = `
# Heading
Some text with special characters
`;

// The parser fails to correctly tokenize certain constructs
// Constructs mapped to specific character codes are being skipped
```

### Expected behavior

The tokenizer should correctly identify and process all constructs based on their character codes. Both character-specific constructs and null-fallback constructs should be evaluated properly.

### Additional context

This appears to affect how the parser handles the construct map lookup. When a specific character code is present, the corresponding construct should be retrieved and processed, but it seems like the logic for combining character-specific and fallback constructs might not be working as intended.

The issue manifests when parsing certain MDX documents where expected syntax elements are not being recognized or processed correctly by the tokenizer.

---
Repository: /testbed
