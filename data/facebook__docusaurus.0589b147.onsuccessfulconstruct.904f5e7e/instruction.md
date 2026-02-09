# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where certain constructs are causing errors due to missing `info.from` property. The parser seems to be calling `onsuccessfulconstruct` with an `info` object that doesn't always have a `from` property defined, which leads to unexpected behavior when trying to add results.

### Reproduction

```js
// When parsing MDX content with specific tokenizer constructs
const parser = createTokenizer(/* ... */);

// The onsuccessfulconstruct callback gets triggered
// but info.from is undefined in some cases
// This causes addResult to be called with undefined
```

### Expected behavior

The tokenizer should handle cases where `info.from` might be undefined gracefully, or ensure that `info.from` is always defined when `onsuccessfulconstruct` is called.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
