# Bug Report

### Describe the bug

I'm experiencing an issue with comma or space separated value parsing in MDX. When parsing strings that contain comma or space separated values, the last character of each token is being truncated, and some tokens are being filtered out unexpectedly.

### Reproduction

```js
// Example input string
const input = "foo bar baz";

// After parsing, getting: ["fo", "ba"]
// Expected: ["foo", "bar", "baz"]
```

Another example:
```js
const input = "item1, item2, item3";

// Getting: ["item", "item"]  
// Expected: ["item1", "item2", "item3"]
```

### Expected behavior

The parser should correctly split comma or space separated strings and return all complete tokens without truncating characters or filtering out valid entries.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
