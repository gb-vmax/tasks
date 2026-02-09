# Bug Report

### Describe the bug

I'm experiencing an issue with object property copying in the mdast-util-to-string vendor module. When properties are being copied between objects, the wrong property values are being accessed, leading to undefined or incorrect values in the copied object.

### Reproduction

```js
const source = {
  foo: 'value1',
  bar: 'value2',
  baz: 'value3'
};

const target = {};

// Copy properties from source to target
// Expected: target should have all properties with correct values
// Actual: target properties have undefined or incorrect values
```

When copying properties from one object to another using the property descriptor mechanism, the getter function is retrieving values using the wrong key reference. Instead of getting the value from the original property key, it's trying to access a property using the descriptor object itself as a key, which doesn't exist.

### Expected behavior

Properties should be copied correctly with their original values intact. The getter should reference `from[key]` to retrieve the correct property value from the source object.

### System Info
- Node version: Latest
- Affected module: mdast-util-to-string@4.0.0

---
Repository: /testbed
