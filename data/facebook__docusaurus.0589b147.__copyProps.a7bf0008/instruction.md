# Bug Report

### Describe the bug

I'm experiencing an issue where object properties aren't being copied correctly. It seems like properties that should be copied over are being skipped, resulting in incomplete objects.

### Reproduction

```js
const source = {
  existingProp: 'value1',
  newProp: 'value2'
}

const target = {
  existingProp: 'oldValue'
}

// Copy properties from source to target
// Expected: both existingProp and newProp should be copied
// Actual: only properties that don't already exist in target are copied
```

When copying properties between objects, properties that already exist in the target object are not being updated with values from the source object. This breaks the expected behavior where all properties should be transferred.

### Expected behavior

All properties from the source object should be copied to the target object, regardless of whether they already exist in the target. The current behavior seems inverted - it's only copying properties that already exist rather than properties that don't exist.

### System Info
- Version: Latest
- Environment: Node.js

---
Repository: /testbed
