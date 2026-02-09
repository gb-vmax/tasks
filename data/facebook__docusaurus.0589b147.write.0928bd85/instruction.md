# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where the tokenizer doesn't properly handle certain input. It seems like the parser is returning empty results when it should be processing the content, or vice versa - the behavior is inconsistent.

### Reproduction

```js
// Create an MDX document with content
const mdxContent = `
# Hello World

Some paragraph text here.
`;

// Try to parse it
const result = compile(mdxContent);

// Expected: parsed tokens/events
// Actual: empty array or incorrect parsing
```

The issue appears to be in the tokenization phase where chunks are being processed. When the last chunk in the array has a certain state, the parser either incorrectly returns an empty array or continues processing when it shouldn't.

### Expected behavior

The tokenizer should correctly identify when to return results vs continue processing. Content should be properly parsed and all tokens/events should be captured.

### Additional context

This might be related to how the tokenizer checks the state of chunks during the write operation. The logic for determining when parsing is complete seems off.

---
Repository: /testbed
