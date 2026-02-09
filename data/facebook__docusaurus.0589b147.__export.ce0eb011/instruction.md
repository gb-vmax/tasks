# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with property enumeration in the remark-gfm vendor module. Properties that should be exported and enumerable are not being properly defined on target objects.

### Reproduction

When using the module's export functionality, properties are being skipped during the export process. This appears to happen when iterating over properties that exist in the prototype chain.

```js
// Example scenario where this breaks:
const target = {};
const source = {
  prop1: () => 'value1',
  prop2: () => 'value2'
};

// Properties should be defined on target but some are being skipped
__export(target, source);

// Expected: target has both prop1 and prop2
// Actual: some properties may be missing
```

### Expected behavior

All properties from the source object should be properly defined on the target object with the correct descriptors (enumerable: true). The export mechanism should not skip properties based on prototype chain checks.

### System Info
- remark-gfm version: 4.0.0
- Environment: Jest test runner

This is causing issues with module loading and property access in our build. Any properties that exist higher up in the prototype chain seem to be affected.

---
Repository: /testbed
