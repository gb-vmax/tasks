# Bug Report

### Describe the bug

I'm experiencing an issue where object expressions are not being included correctly in the output bundle. It seems like the inclusion logic is broken - objects that should be included in the final bundle are missing, leading to runtime errors or incomplete code generation.

### Reproduction

```js
// Example code that triggers the issue
const obj = {
  prop1: someValue,
  prop2: anotherValue
};

// When this object expression should be included in the bundle,
// it's not being added properly
export { obj };
```

The object expression gets skipped during the inclusion phase even though it's clearly referenced and should be part of the output.

### Expected behavior

Object expressions that are referenced should be properly included in the bundle. The inclusion logic should mark the node as included before processing its entity and properties.

### Additional context

This appears to be a regression - it was working fine in previous versions. The issue manifests when object expressions need to be included in the bundle but aren't being marked correctly during the tree-shaking phase.

---
Repository: /testbed
