# Bug Report

### Describe the bug

I'm experiencing an issue with object property copying where properties that should be excluded are being copied instead, and properties that should be included are being skipped.

When using the library's internal property copying mechanism, the behavior is inverted - excluded properties appear in the target object while all other properties are missing.

### Reproduction

```js
const source = {
  foo: 'value1',
  bar: 'value2',
  baz: 'value3'
}

const target = {}

// Try to copy all properties except 'bar'
// Expected: target should have 'foo' and 'baz'
// Actual: target only has 'bar'
copyProperties(target, source, 'bar')

console.log(target)
// Expected: { foo: 'value1', baz: 'value3' }
// Actual: { bar: 'value2' }
```

### Expected behavior

When copying properties with an exception parameter, all properties except the specified one should be copied to the target object. Currently it's doing the opposite - only copying the property that should be excluded.

### System Info
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
