# Bug Report

### Describe the bug

I'm experiencing an issue with parsing identifiers in MDX files. When using keywords like `class` or `function` as property names in object notation (e.g., `obj.class` or `obj.function`), the parser seems to be handling them incorrectly.

### Reproduction

```js
const obj = {
  class: 'my-class',
  function: () => {}
}

// Accessing these properties
obj.class
obj.function
```

When this code is used in an MDX file, the parser doesn't seem to recognize these as valid property accesses. The issue appears to be related to how the parser distinguishes between keywords used as identifiers vs actual keyword usage.

### Expected behavior

Keywords should be allowed as property names when accessed via dot notation (e.g., `obj.class` should be valid). This is standard JavaScript behavior and should work in MDX as well.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
