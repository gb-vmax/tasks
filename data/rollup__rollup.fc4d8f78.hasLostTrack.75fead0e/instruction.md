# Bug Report

### Describe the bug

I'm experiencing an issue with object property tracking in the bundler. It seems like the tracking state is getting inverted in certain scenarios, causing properties to be incorrectly marked as tracked or untracked.

### Reproduction

```js
// Create an object entity with property tracking
const obj = {
  nested: {
    prop: 'value'
  }
}

// Access nested properties multiple times
obj.nested.prop
obj.nested.prop

// The tracking state appears to flip unexpectedly
// Properties that should be tracked are marked as untracked and vice versa
```

### Expected behavior

Property tracking should maintain consistent state. When a property is accessed, it should be marked as tracked and remain tracked. The tracking flag should not flip based on whether it was already set to that value.

### System Info

- Rollup version: Latest
- Node version: 18.x

This is causing issues with tree-shaking optimization where properties are either incorrectly retained or incorrectly removed from the bundle. The behavior seems to have changed recently and is affecting the correctness of the bundled output.

---
Repository: /testbed
