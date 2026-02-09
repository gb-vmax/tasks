# Bug Report

### Describe the bug

I'm encountering an issue with parsing numeric literals that end with `n` (BigInt literals). The parser seems to be incorrectly handling the raw string representation and the bigint value extraction.

### Reproduction

```js
// When parsing a BigInt literal like:
const value = 123n;

// Or with underscores:
const largeValue = 1_000_000n;
```

The parsed AST node's `raw` property appears to be missing the last character, and when extracting the bigint value, the digits themselves are being removed instead of just the underscore separators.

### Expected behavior

For a BigInt literal like `123n`:
- The `raw` property should be `"123n"` (the complete literal as written)
- The `bigint` property should be `"123"` (just the numeric value without the `n` suffix)

For a BigInt literal with separators like `1_000_000n`:
- The `raw` property should be `"1_000_000n"`
- The `bigint` property should be `"1000000"` (numeric value with underscores removed)

### System Info
- Package: @mdx-js/mdx@3.0.0
- Node version: Latest

This seems to have broken after a recent change to the literal parsing logic. The bigint extraction is producing unexpected results.

---
Repository: /testbed
