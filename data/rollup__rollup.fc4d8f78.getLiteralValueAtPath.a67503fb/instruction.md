# Bug Report

### Describe the bug

When accessing the `Symbol.toStringTag` property on namespace imports, the returned value is incorrect. It should return `'Module'` but instead returns `'Object'`.

### Reproduction

```js
import * as myNamespace from './module';

// Checking the toStringTag
console.log(Object.prototype.toString.call(myNamespace));
// Expected: '[object Module]'
// Actual: '[object Object]'
```

This affects code that relies on proper type detection of namespace objects, particularly when using `Object.prototype.toString.call()` for type checking.

### Expected behavior

Namespace imports should be identified as `'Module'` when their `Symbol.toStringTag` is accessed, not as `'Object'`. This is important for maintaining proper type semantics and compatibility with module introspection patterns.

### Additional context

This seems to have broken recently. The namespace object should properly identify itself as a Module type when inspected.

---
Repository: /testbed
