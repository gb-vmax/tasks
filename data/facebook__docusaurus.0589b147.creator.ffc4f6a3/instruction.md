# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where tokenizers aren't being invoked correctly. The parser seems to be returning a function that wraps the tokenizer instead of returning the tokenizer itself, which breaks the parsing flow.

### Reproduction

```js
const mdx = require('@mdx-js/mdx');

const content = `
# Hello World

This is a test MDX document.
`;

// Attempting to parse MDX content
const result = mdx.compile(content);
```

When the parser tries to use the tokenizer, it receives a function wrapper instead of the actual tokenizer object, causing the parsing to fail or behave unexpectedly.

### Expected behavior

The parser should receive and use the tokenizer directly to process the MDX content. The tokenizer creation should return the tokenizer instance itself, not a wrapper function around it.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
