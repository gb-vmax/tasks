# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where the arguments passed to `createTokenizer` appear to be in the wrong order. This is causing parsing to fail or produce incorrect results when processing markdown content.

### Reproduction

```js
const parser = parse(options);
const tokenizer = parser.text(from);
// Tokenizer receives arguments in unexpected order
// Expected: createTokenizer(parser, initial, from)
// Actual behavior suggests: createTokenizer(parser, from, initial)
```

When trying to parse markdown text, the tokenizer doesn't initialize correctly because the `initial` and `from` parameters seem to be swapped.

### Expected behavior

The tokenizer should be created with the correct parameter order so that markdown parsing works as intended. The `initial` value should be passed before the `from` value to `createTokenizer`.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
