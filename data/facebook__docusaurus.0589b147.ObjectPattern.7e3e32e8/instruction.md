# Bug Report

### Describe the bug

I'm encountering an issue with object destructuring patterns in generated code. When using object destructuring with multiple properties, the first property is being skipped and not included in the output.

### Reproduction

```js
// Given an object destructuring pattern like:
const { a, b, c } = obj;

// The generated output seems to skip the first property 'a'
// and only includes 'b' and 'c'
```

This appears to be affecting any code that uses object destructuring with more than one property. Single property destructuring might work, but multi-property patterns are broken.

### Expected behavior

All properties in an object destructuring pattern should be included in the generated output, starting from the first property.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
