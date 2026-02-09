# Bug Report

### Describe the bug

I'm experiencing an issue with text parsing in MDX where the data tokenizer seems to be exiting at the wrong time. When processing text content, the tokenizer appears to be calling `effects.exit("data")` before consuming the final character, which breaks the expected token structure.

### Reproduction

```js
// When parsing MDX content with text data
const content = `Some text content here`

// The tokenizer processes characters but exits the "data" state
// before consuming the last character in the sequence
```

This causes the text parsing to behave incorrectly - it looks like the exit is happening after consuming each character instead of after the entire data segment is processed.

### Expected behavior

The tokenizer should:
1. Consume all characters in the data segment
2. Exit the "data" state only when a break is detected
3. Return to the appropriate continuation state

Instead, it seems to be exiting the data state prematurely, which disrupts the token flow.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
