# Bug Report

### Describe the bug

The `deterministicStringify` function is producing incorrect output when serializing objects and arrays. It appears that empty string values in objects are now being included in the output when they should be filtered out, and array items are being handled in reverse - empty items are included while non-empty ones are excluded.

### Reproduction

```js
import { deterministicStringify } from './deterministicStringify';

// Test with object containing empty values
const obj = {
  name: 'test',
  value: '',
  id: '123'
};

console.log(deterministicStringify(obj));
// Expected: {"id":"123","name":"test"}
// Actual: includes empty value field

// Test with array containing various values
const arr = ['hello', 'world', 'test'];

console.log(deterministicStringify(arr));
// Expected: ["hello","world","test"]
// Actual: returns empty array or incorrect items
```

### Expected behavior

1. Object properties with empty string values should be filtered out from the serialized output
2. Array items with non-empty values should be included in the serialized output
3. The function should produce deterministic, consistent JSON strings for the same input

### Additional context

This seems to have broken the sync functionality as objects are no longer being serialized correctly. The deterministic stringification is critical for generating consistent hashes and comparing objects.

---
Repository: /testbed
