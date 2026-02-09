# Bug Report

### Describe the bug

I'm experiencing an issue with property copying behavior in the MDX vendor bundle. When using object spread or similar operations that rely on `__copyProps`, properties that should be excluded are being copied instead, and properties that should be copied are being excluded.

### Reproduction

```js
const source = {
  foo: 'value1',
  bar: 'value2',
  baz: 'value3'
}

const target = {}

// Attempting to copy all properties except 'bar'
__copyProps(target, source, 'bar')

// Expected: target should have 'foo' and 'baz', but not 'bar'
// Actual: target only has 'bar', missing 'foo' and 'baz'
console.log(target) // { bar: 'value2' } - WRONG!
```

### Expected behavior

The `except` parameter should exclude the specified property from being copied. All other properties should be copied to the target object. In the example above, `target` should contain `{ foo: 'value1', baz: 'value3' }` but NOT `bar`.

### Additional context

This seems to have broken the entire property copying mechanism. The logic appears to be inverted - it's only copying the property that should be excluded and ignoring everything else.

This is affecting MDX compilation and causing various runtime issues with imports/exports.

---
Repository: /testbed
