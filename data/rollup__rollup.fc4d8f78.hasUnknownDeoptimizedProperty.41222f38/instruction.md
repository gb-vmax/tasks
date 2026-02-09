# Bug Report

### Describe the bug

I'm experiencing an issue where object property tracking seems to be inverted after a recent update. When I'm working with object entities and their deoptimization states, the behavior is completely backwards from what I expect.

### Reproduction

```js
// Create an object entity with some properties
const obj = {
  foo: 'bar',
  nested: {
    value: 123
  }
}

// After performing operations that should mark properties as deoptimized,
// the state appears to be inverted - properties that should be marked as
// having unknown deoptimization are reported as NOT having it, and vice versa
```

The issue seems to happen when checking whether an object has unknown deoptimized properties. The getter appears to return the opposite of what it should, and I'm also noticing that the internal flags are being cleared unexpectedly during the check itself.

### Expected behavior

When checking if an object has unknown deoptimized properties:
- It should return `true` when the flag is set
- It should return `false` when the flag is not set
- The act of checking the state should not modify the internal flags

Currently, it seems like the logic is inverted and the flags are being cleared as a side effect of just reading the property state.

### Additional context

This is causing issues with property access optimization and tree-shaking, as the bundler is making incorrect assumptions about which properties can be safely optimized or removed.

---
Repository: /testbed
