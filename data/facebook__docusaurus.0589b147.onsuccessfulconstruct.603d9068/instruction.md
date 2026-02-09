# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where tokenization appears to be broken. When processing MDX content, the parser seems to be using incorrect position information, which causes the tokenizer to fail or produce unexpected results.

### Reproduction

```js
// Parse MDX content with nested constructs
const mdx = `
# Hello

Some content with **bold** text.
`;

const result = compile(mdx);
// Parser fails to correctly identify token positions
```

### Expected behavior

The tokenizer should correctly track and use the original position information (`info.from`) when processing successful constructs. The parsed output should maintain proper token boundaries and positions.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken recently. The tokenizer is not using the right position data when calling `addResult`, which affects how constructs are processed and stored.

---
Repository: /testbed
