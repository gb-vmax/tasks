# Bug Report

### Describe the bug

When copying properties between objects, some properties that should be copied are being skipped. It looks like the property enumeration logic is checking the wrong object for property ownership, causing valid properties from the source object to be excluded from the copy operation.

### Reproduction

```js
const source = {
  prop1: 'value1',
  prop2: 'value2',
  prop3: 'value3'
};

const target = {
  prop1: 'existing'
};

// Copy properties from source to target
// Expected: prop2 and prop3 should be copied
// Actual: Properties are not being copied correctly
```

### Expected behavior

All enumerable properties from the source object that don't already exist on the target should be copied over. The function should check if the property exists on the target object (not the source) before deciding whether to copy it.

### System Info
- Version: latest
- Environment: Node.js

---
Repository: /testbed
