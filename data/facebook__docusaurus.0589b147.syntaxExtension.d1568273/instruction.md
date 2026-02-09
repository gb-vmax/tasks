# Bug Report

### Describe the bug

I'm experiencing an issue with syntax extensions where constructs are being duplicated or overwritten incorrectly. When registering multiple syntax extensions, it seems like the extension merging logic isn't working as expected.

### Reproduction

```js
const extension1 = {
  flow: {
    [42]: myConstruct1
  }
}

const extension2 = {
  flow: {
    [42]: myConstruct2
  }
}

// When merging these extensions, constructs aren't being combined properly
// Expected: both constructs should be in the array
// Actual: constructs are being overwritten or duplicated unexpectedly
```

### Expected behavior

When multiple syntax extensions define constructs for the same code point, they should be properly merged into an array. Each construct should appear once in the final array, and existing constructs shouldn't be overwritten.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have started happening recently. The syntax extension merging behavior appears to be inverted or incorrect.

---
Repository: /testbed
