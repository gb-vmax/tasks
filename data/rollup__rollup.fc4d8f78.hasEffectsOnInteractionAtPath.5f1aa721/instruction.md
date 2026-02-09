# Bug Report

### Describe the bug

I'm experiencing incorrect behavior when accessing nested object properties in certain scenarios. It seems like the property access path is being evaluated in the wrong order, causing side effects to be checked against incorrect paths.

### Reproduction

```js
const obj = {
  nested: {
    deep: {
      value: 'test'
    }
  }
}

// When checking side effects on nested property access
// The path resolution appears to be reversed
// Expected: ['nested', 'deep', 'value']
// Actual behavior suggests: ['value', 'nested', 'deep']
```

This leads to incorrect side effect detection when dealing with object member expressions that have multiple levels of nesting.

### Expected behavior

The property access path should be constructed in the correct order (parent path first, then member path), so that side effects are properly tracked through the entire chain of property accesses.

### Additional context

This appears to affect how the bundler analyzes side effects in code with deeply nested object member expressions. The issue manifests when the order of path concatenation matters for determining whether an interaction has effects.

---
Repository: /testbed
