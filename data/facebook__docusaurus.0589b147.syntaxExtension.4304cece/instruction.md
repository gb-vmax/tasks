# Bug Report

### Describe the bug

I'm encountering an issue with the MDX syntax extension handling where custom syntax extensions are not being properly merged. When trying to register multiple syntax constructs for the same code point, the extensions seem to be overwriting each other instead of being combined.

### Reproduction

```js
const extension1 = {
  flow: {
    42: someConstruct
  }
}

const extension2 = {
  flow: {
    42: anotherConstruct
  }
}

// After merging these extensions, only one construct is preserved
// instead of having both constructs available for code point 42
const combined = syntaxExtension(extension1, extension2)
```

### Expected behavior

When multiple extensions define constructs for the same code point, they should be combined into an array so that all constructs are available. Currently it appears that existing constructs are being replaced instead of extended.

### Additional context

This seems to affect any scenario where you want to have multiple parsing constructs handle the same character code, which is a pretty common use case when composing MDX extensions.

---
Repository: /testbed
