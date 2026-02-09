# Bug Report

### Describe the bug

I'm encountering an issue with the MDX parser where it's creating empty token entries even when there's no whitespace to consume. The `factorySpace` function now always calls `effects.enter(type)` regardless of whether any markdown space is actually present.

### Reproduction

```js
// When parsing content without leading/trailing spaces
const content = `# Hello World`;

// The parser creates an empty space token entry
// even though no space characters are present
```

This is causing unnecessary token entries in the AST which can affect downstream processing and potentially break certain parsers that expect space tokens to only exist when actual whitespace is consumed.

### Expected behavior

The `effects.enter(type)` should only be called when `markdownSpace(code2)` returns true, meaning actual whitespace is detected. Empty space tokens shouldn't be created when there's no whitespace to process.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
