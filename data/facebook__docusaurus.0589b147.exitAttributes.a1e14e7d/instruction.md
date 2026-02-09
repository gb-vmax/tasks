# Bug Report

### Describe the bug

I'm experiencing an issue with class attribute handling in remark-directive. When multiple class directives are specified, they seem to be concatenated in the wrong order, and there might also be an issue with how existing class values are being handled.

### Reproduction

```js
// When parsing directives with multiple class attributes
// Expected: classes in the order they appear
// Actual: classes appear in reverse order or with unexpected spacing

const directive = parseDirective('::example{.first .second .third}')
// The class attribute ends up being ordered incorrectly
```

I noticed this when using multiple class directives - the order of classes in the final output doesn't match the order they were specified in the source. Additionally, there seems to be some inconsistency in how the class string is being built up.

### Expected behavior

Classes should be concatenated in the order they appear in the source, and the concatenation logic should properly handle existing class values.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
