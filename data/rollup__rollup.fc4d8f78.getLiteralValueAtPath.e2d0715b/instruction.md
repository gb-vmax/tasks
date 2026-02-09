# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking when using the `in` operator with namespace imports. It appears that exports are being incorrectly removed from the bundle even when they're being checked for existence using the `in` operator.

### Reproduction

```js
import * as ns from './module';

// Check if export exists
if ('someExport' in ns) {
  console.log('Export exists');
} else {
  console.log('Export does not exist');
}
```

When `someExport` is actually defined in the module, the condition incorrectly evaluates to `false` and the bundle behaves as if the export doesn't exist.

### Expected behavior

The `in` operator should correctly detect whether a named export exists in the namespace object. If `someExport` is defined in the module, the condition should evaluate to `true`.

### Additional context

This seems to affect the tree-shaking optimization for namespace imports. The bundler appears to be making incorrect assumptions about which exports are actually used.

---
Repository: /testbed
