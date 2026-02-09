# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX tokenizer where `sliceStream` crashes when `chunks` is undefined or null. This appears to happen in certain edge cases during parsing, causing the entire parsing process to fail unexpectedly.

### Reproduction

The error occurs when the tokenizer's `sliceStream` function is called before `chunks` has been properly initialized. This can happen with malformed or unusual MDX input that triggers early tokenization.

```js
// Example scenario that triggers the issue
const parser = createTokenizer(/* ... */);
// When sliceStream is called with chunks being undefined
const result = sliceStream(token);
// Results in: TypeError: Cannot read property 'length' of undefined
```

### Expected behavior

The tokenizer should handle cases where `chunks` might not be initialized yet, either by returning an empty array or properly initializing the chunks before attempting to slice them. The parser shouldn't crash on edge cases.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems like it could be a regression or an edge case that wasn't previously accounted for. The function is trying to access `chunks` without checking if it exists first.

---
Repository: /testbed
