# Bug Report

### Describe the bug
I'm experiencing an issue with member expression path resolution where the order of path keys appears to be reversed. When accessing nested properties like `obj.prop1.prop2`, the path seems to be constructed in the wrong order, which affects source map positions and potentially other features that rely on accurate path tracking.

### Reproduction
```js
// Given a member expression like:
const value = myObject.nested.property;

// The path resolution returns keys in reverse order:
// Expected: ['myObject', 'nested', 'property']
// Actual: ['property', 'nested', 'myObject']
```

This affects any code that relies on the correct ordering of member expression paths, particularly when dealing with deeply nested property access.

### Expected behavior
The path should be constructed in the correct left-to-right order, matching the actual structure of the member expression. Source positions should also correspond to the correct parts of the expression.

### Additional context
This seems to have started after a recent change to the `getPathIfNotComputed` function. The issue is particularly noticeable when working with complex nested object access patterns.

---
Repository: /testbed
