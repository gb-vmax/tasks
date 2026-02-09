# Bug Report

### Describe the bug

I'm experiencing an issue with MDX syntax extensions where custom syntax handlers are not being registered correctly. When trying to use multiple syntax extensions together, some of them seem to be getting overwritten or ignored completely.

### Reproduction

```js
const extension1 = {
  flow: {
    123: { tokenize: tokenizer1 }
  }
}

const extension2 = {
  flow: {
    123: { tokenize: tokenizer2 }
  }
}

const combined = combineExtensions([extension1, extension2])
// Expected: both tokenizers should be available
// Actual: only one tokenizer is registered
```

When combining extensions that target the same character codes, the extensions don't get merged properly. It seems like existing handlers are being replaced instead of combined into an array.

### Expected behavior

All syntax extensions should be properly combined and available when using `combineExtensions()`. Multiple handlers for the same character code should coexist in an array.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
