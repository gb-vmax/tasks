# Bug Report

### Describe the bug

I'm encountering unexpected behavior when accessing properties on objects that don't exist. It seems like member expressions are incorrectly reporting their undefined status, causing the bundler to make wrong assumptions about property access.

### Reproduction

```js
const obj = {};
const result = obj.nonExistentProperty;

// Expected: Should be treated as undefined access
// Actual: Seems to be treated as a defined property
```

This appears to affect tree-shaking and dead code elimination. Code that should be removed because it accesses undefined properties is being kept in the bundle, or vice versa.

### Expected behavior

When accessing a property that doesn't exist on an object, the member expression should correctly identify this as an undefined access. This is important for proper optimization and code generation.

### Additional context

This might be related to how the AST handles property existence checks. The issue seems to affect both computed and non-computed member expressions.

---
Repository: /testbed
