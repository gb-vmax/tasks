# Bug Report

### Describe the bug

I'm experiencing an issue with object property copying in the mdast-util-to-string vendor module. When properties are being copied from one object to another, the wrong values are being retrieved, causing unexpected behavior in downstream code.

### Reproduction

```js
const source = {
  foo: 'value1',
  bar: 'value2'
}

const target = {}

// Copy properties from source to target
// Expected: target.foo === 'value1', target.bar === 'value2'
// Actual: All properties reference the same incorrect value
```

The issue appears to be in the property copying logic where properties are being defined with getters. Instead of getting the correct property value from the source object, it seems to be retrieving values using the wrong key.

### Expected behavior

When copying properties between objects, each property should retain its original value from the source object. Accessing `target.foo` should return the value of `source.foo`, and `target.bar` should return the value of `source.bar`.

### System Info
- Version: Latest from main branch
- Affected file: `jest/vendor/mdast-util-to-string@4.0.0.js`

This is causing issues when working with markdown AST transformations where object properties need to be accurately copied.

---
Repository: /testbed
