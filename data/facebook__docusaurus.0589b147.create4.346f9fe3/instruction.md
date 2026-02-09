# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the tokenizer seems to be receiving arguments in the wrong order. This is causing parsing failures for certain MDX content that previously worked fine.

### Reproduction

```js
// When parsing MDX content with custom tokenizers
const result = parse({
  // MDX content with custom syntax
});

// The tokenizer receives arguments in unexpected order
// Expected: createTokenizer(parser, initial, from)
// Actual: createTokenizer(parser, from, initial)
```

The issue appears to be in the `create4` function where the `creator` function is being called without the `from` parameter, and then the parameters are being passed to `createTokenizer` in the wrong order.

### Expected behavior

The tokenizer should receive the `initial` and `from` parameters in the correct order so that MDX content is parsed correctly without errors.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
