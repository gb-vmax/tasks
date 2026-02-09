# Bug Report

### Describe the bug
When using `deterministicStringify()` on objects and arrays, the output is incorrect. Empty string values are being excluded when they should be included, and the logic for filtering key-value pairs appears to be inverted.

### Reproduction
```js
// Object with empty string value
const obj = { key: '' };
const result = deterministicStringify(obj);
// Expected: '{"key":""}'
// Actual: '{}'

// Array with empty strings
const arr = ['test', '', 'value'];
const result2 = deterministicStringify(arr);
// Expected: '["test","","value"]'
// Actual: '["test","value"]' (empty string is missing)

// Object with both empty and non-empty values
const mixed = { a: 'value', b: '', c: 'another' };
const result3 = deterministicStringify(mixed);
// The key-value pairs are not being filtered correctly
```

### Expected behavior
- Empty string values should be preserved in the output
- Objects should include key-value pairs where either the key or value is non-empty
- Arrays should include all elements, including empty strings

### Additional context
This seems to have broken the deterministic serialization logic. The function is now excluding valid data that should be included in the stringified output.

---
Repository: /testbed
