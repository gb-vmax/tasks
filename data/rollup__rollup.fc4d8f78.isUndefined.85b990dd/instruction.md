# Bug Report

### Describe the bug

I'm encountering an issue where member expressions are incorrectly being treated as defined when they should be undefined. This seems to be causing problems with dead code elimination and tree-shaking in my build output.

### Reproduction

```js
const obj = {};
const result = obj.nonExistentProperty?.someMethod();

// Expected: result should be undefined
// Actual: the code behaves as if the property exists
```

When accessing properties that don't exist on an object, the AST seems to be marking them as defined rather than undefined. This is affecting optional chaining behavior and causing code that should be eliminated to remain in the bundle.

### Expected behavior

Member expressions that reference non-existent properties should be correctly identified as undefined, allowing proper tree-shaking and dead code elimination.

### Additional context

This appears to have started recently. The issue manifests when using optional chaining or when the bundler tries to determine if certain code paths can be eliminated. Properties that clearly don't exist are being treated as if they might have values.

---
Repository: /testbed
