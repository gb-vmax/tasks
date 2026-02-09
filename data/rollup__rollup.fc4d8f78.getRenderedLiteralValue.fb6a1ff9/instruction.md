# Bug Report

### Describe the bug

The `in` operator optimization for namespace variables seems to be broken. When checking if a property exists in a namespace using the `in` operator, the code is not being optimized correctly and returns `UnknownValue` instead of the actual literal value.

### Reproduction

```js
// Given a namespace variable
import * as ns from './module';

// This should be optimized but isn't
if ('export' in ns) {
  // ...
}
```

The condition should be evaluated at compile time when checking for known exports in a namespace, but it appears the optimization is being skipped.

### Expected behavior

When using the `in` operator with namespace variables to check for known exports, the expression should be optimized to a literal boolean value at compile time rather than remaining as `UnknownValue`.

### Additional context

This affects tree-shaking and dead code elimination since the bundler can't determine which branches are actually reachable when the `in` operator is used with namespaces.

---
Repository: /testbed
