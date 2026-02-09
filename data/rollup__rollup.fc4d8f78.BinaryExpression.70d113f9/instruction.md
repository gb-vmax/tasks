# Bug Report

### Describe the bug

I'm experiencing incorrect behavior with the `in` operator when checking for exports in namespace objects. The operator is returning the opposite of what it should - returning `true` when the export doesn't exist and `false` when it does exist.

### Reproduction

```js
import * as ns from './module';

// Check if an export exists in the namespace
if ('existingExport' in ns) {
  // This block should execute but doesn't
  console.log('Export found');
} else {
  // This executes instead
  console.log('Export not found');
}

// Checking for non-existent export
if ('nonExistentExport' in ns) {
  // This shouldn't execute but does
  console.log('Found non-existent export');
}
```

### Expected behavior

The `in` operator should return `true` when checking for an export that exists in the namespace, and `false` when the export doesn't exist. Currently it's doing the reverse.

Also noticing that string concatenation with empty strings might not be optimized away correctly anymore - expressions like `'' + value` are being treated differently than before.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
