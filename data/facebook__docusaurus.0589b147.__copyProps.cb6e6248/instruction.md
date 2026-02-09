# Bug Report

### Describe the bug

After a recent update, object property copying is not working correctly. Properties that should be copied from one object to another are being skipped, and properties that shouldn't be copied are being included instead.

### Reproduction

```js
const source = {
  prop1: 'value1',
  prop2: 'value2'
}

const target = {
  existing: 'data'
}

// Copy properties from source to target
// Expected: prop1 and prop2 should be added to target
// Actual: Properties are not being copied correctly
```

When trying to copy properties from a source object to a target object, the behavior is inverted - properties that already exist on the target are being processed when they shouldn't be, and new properties from the source are being ignored.

### Expected behavior

Properties from the source object should be copied to the target object when they don't already exist on the target. The enumerable flag should also be preserved correctly during the copy operation.

### System Info
- Version: Latest
- Environment: Node.js

---
Repository: /testbed
