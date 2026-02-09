# Bug Report

### Describe the bug

I'm experiencing an issue with the `in` operator when used with namespace variables. It seems like the optimization for `'export' in ns` expressions is not working correctly - the bundler is not properly detecting these cases and they're being treated as unknown values instead of being optimized.

### Reproduction

```js
// Input code
import * as ns from './module.js';

if ('someExport' in ns) {
  console.log('Export exists');
}
```

Expected: The bundler should optimize this check since it can statically determine if the export exists in the namespace.

Actual: The expression is treated as an unknown value and not optimized during the build process.

### Expected behavior

When checking if an export exists in a namespace using the `in` operator (e.g., `'export' in ns`), the bundler should be able to evaluate this at build time and optimize accordingly, since namespace exports are statically analyzable.

### Additional context

This appears to affect tree-shaking and dead code elimination for code that conditionally uses namespace exports. The optimization should work for expressions like:
- `'foo' in namespaceVariable`
- Checking for specific named exports in imported namespaces

---
Repository: /testbed
