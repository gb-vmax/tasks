# Bug Report

### Describe the bug

I'm encountering an issue with the MDX tokenizer where the return state is not being handled correctly. After recent changes, the tokenizer appears to be returning the wrong value in certain parsing scenarios, which breaks the parsing flow.

### Reproduction

When parsing MDX content with specific token patterns, the tokenizer's `ok3` callback function returns an unexpected value. This causes the parser to fail or behave incorrectly during content processing.

Example scenario:
```js
// Parse MDX content with nested constructs
const result = compile(mdxContent, options);
// Parser flow breaks due to incorrect return value
```

The issue seems to be related to how the tokenizer handles successful token consumption and what value it returns to continue the parsing state machine.

### Expected behavior

The tokenizer should return the correct state value (`returnState`) to allow the parser to continue processing subsequent tokens properly. The parsing flow should proceed as expected without breaking.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
