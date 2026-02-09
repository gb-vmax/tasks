# Bug Report

### Describe the bug

I'm experiencing an issue where object properties are not being properly tracked for side effects after deoptimization. It seems like the internal state management for deoptimized properties is getting inverted somehow.

### Reproduction

```js
// Create an object with nested properties
const obj = {
  foo: {
    bar: 'value'
  }
}

// Access and modify the property
obj.foo.bar = 'new value'

// Expected: Property changes should be tracked correctly
// Actual: Property tracking appears to be inverted
```

When working with objects that have been deoptimized (e.g., after dynamic property access), subsequent property accesses don't behave as expected. The tracking state seems to be flipped - properties that should be marked as having unknown deoptimization are not, and vice versa.

### Expected behavior

Object entities should correctly track whether they have unknown deoptimized properties. When a property is deoptimized, the flag should be set appropriately and property accesses should be handled correctly.

### System Info

- Rollup version: latest
- Node version: 18.x

This is affecting tree-shaking behavior in my project where objects with dynamic property access are not being handled correctly.

---
Repository: /testbed
