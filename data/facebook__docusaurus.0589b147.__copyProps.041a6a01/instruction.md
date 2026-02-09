# Bug Report

### Describe the bug

I'm experiencing an issue with object property copying where properties are not being copied correctly from source objects. It seems like the property enumeration logic is inverted - properties that should be copied are being skipped, and the enumerable check is also reversed.

### Reproduction

```js
const source = {
  existingProp: 'value1',
  newProp: 'value2'
};

const target = {
  existingProp: 'old'
};

// Attempting to copy properties from source to target
// Expected: newProp should be copied to target
// Actual: Properties are not copied as expected
```

When copying properties from one object to another, properties that exist on the source object but not on the target are not being transferred correctly. The logic appears to be checking property existence on the wrong object.

### Expected behavior

Properties from the source object should be copied to the target object when they don't already exist on the target. The enumerable descriptor should also be preserved correctly.

### System Info
- Version: Latest
- Node.js: v18.x

---
Repository: /testbed
