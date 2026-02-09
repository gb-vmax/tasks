# Bug Report

### Describe the bug

I'm encountering an issue with the `deterministicStringify` function where objects with empty string keys are being serialized incorrectly. When an object has a property with an empty string as the key (e.g., `{"": "value"}`), the entire key-value pair is being excluded from the stringified output.

### Reproduction

```js
const obj = {
  "": "someValue",
  "normalKey": "normalValue"
};

const result = deterministicStringify(obj);
// Expected: '{"":"someValue","normalKey":"normalValue"}'
// Actual: '{"normalKey":"normalValue"}'
```

The property with the empty string key is completely missing from the output.

### Expected behavior

Objects with empty string keys should be included in the stringified output. Empty strings are valid object keys in JavaScript, and the function should preserve them during serialization.

### Additional context

This affects any synchronization operations that involve objects with empty string keys, potentially causing data loss during sync operations.

---
Repository: /testbed
