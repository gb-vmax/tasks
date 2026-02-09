# Bug Report

### Describe the bug

I'm experiencing an issue with property copying in the rehype-stringify vendor module. When using the library, properties from source objects are not being correctly transferred to target objects. The getter functions seem to be referencing the wrong variable, causing unexpected behavior when accessing copied properties.

### Reproduction

```js
const source = {
  prop1: 'value1',
  prop2: 'value2',
  prop3: 'value3'
};

const target = {};

// After copying properties using __copyProps
// Accessing target.prop1, target.prop2, target.prop3 all return the same value
// instead of their respective values
```

### Expected behavior

Each property on the target object should return its corresponding value from the source object. For example:
- `target.prop1` should return `'value1'`
- `target.prop2` should return `'value2'`
- `target.prop3` should return `'value3'`

Instead, all properties seem to return the same value (the last iterated property).

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

This appears to be related to how property descriptors are being defined during the copy operation. The issue manifests when trying to access any copied properties - they don't return the expected values.

---
Repository: /testbed
