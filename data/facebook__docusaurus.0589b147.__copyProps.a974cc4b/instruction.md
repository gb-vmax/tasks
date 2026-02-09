# Bug Report

### Describe the bug

I'm experiencing an issue with object property copying in the rehype-stringify vendor module. After a recent update, it appears that properties are not being copied correctly between objects. The behavior seems inverted - properties that should be copied are being skipped, and properties that already exist are being overwritten.

### Reproduction

```js
const target = { existingProp: 'original' };
const source = { newProp: 'value', existingProp: 'updated' };

// Copy properties from source to target
// Expected: newProp should be added, existingProp should remain 'original'
// Actual: newProp is not added, existingProp gets overwritten to 'updated'
```

The issue manifests when trying to extend objects with new properties while preserving existing ones. It looks like the logic for checking whether a property should be copied has been reversed somehow.

### Expected behavior

Properties from the source object should only be copied to the target object if they don't already exist on the target. Existing properties on the target should be preserved and not overwritten.

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

---
Repository: /testbed
