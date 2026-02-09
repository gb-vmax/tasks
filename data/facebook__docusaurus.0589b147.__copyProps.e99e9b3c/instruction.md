# Bug Report

### Describe the bug

I'm experiencing an issue with property copying in the remark-directive vendor module. When using the module's internal `__copyProps` function, properties are being copied incorrectly - it seems like properties that should be excluded are being included, and vice versa.

### Reproduction

```js
const source = {
  foo: 'bar',
  baz: 'qux',
  excluded: 'should not copy'
}

const target = {}

// Try to copy all properties except 'excluded'
__copyProps(target, source, 'excluded')

// Expected: target should have 'foo' and 'baz', but NOT 'excluded'
// Actual: target only has 'excluded', missing 'foo' and 'baz'
console.log(target) // { excluded: 'should not copy' }
```

### Expected behavior

The `except` parameter should exclude the specified property from being copied. All other properties from the source object should be copied to the target object. Currently it's doing the opposite - only copying the property that should be excluded.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

This is breaking module exports and causing properties to not be available when they should be.

---
Repository: /testbed
