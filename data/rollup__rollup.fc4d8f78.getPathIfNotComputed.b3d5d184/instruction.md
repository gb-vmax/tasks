# Bug Report

### Describe the bug

I'm experiencing an issue with member expression paths where the position information seems to be incorrect or missing when accessing nested object properties. The path positions don't match what I'd expect when working with chained property access.

### Reproduction

```js
const obj = {
  foo: {
    bar: {
      baz: 'value'
    }
  }
}

// When accessing obj.foo.bar
// The path positions are swapped/incorrect
// Expected: positions should correspond to their respective keys
```

### Expected behavior

When accessing nested properties like `obj.foo.bar`, each key in the path should have the correct position information that corresponds to where that specific property appears in the source code. Currently, the positions seem to be assigned incorrectly.

Additionally, for deeply nested member expressions (more than 2 levels), the path seems to be incomplete - it's not including all the keys in the chain.

### Additional context

This appears to affect how source positions are tracked for member expressions, which could impact error reporting and source mapping. The issue manifests with both simple two-level access (`obj.foo`) and deeper nesting (`obj.foo.bar.baz`).

---
Repository: /testbed
