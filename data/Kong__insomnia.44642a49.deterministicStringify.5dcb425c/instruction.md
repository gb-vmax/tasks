# Bug Report

### Describe the bug
The `deterministicStringify` function is not handling empty strings and falsy values correctly in objects and arrays. When an object has a key or value that is an empty string, or when an array contains empty string elements, they are now being included in the output when they should be filtered out.

### Reproduction
```js
const obj = {
  name: 'test',
  empty: '',
  value: 'data'
}

const result = deterministicStringify(obj);
// Now includes empty string entries that shouldn't be there
```

```js
const arr = ['item1', '', 'item2', ''];

const result = deterministicStringify(arr);
// Empty strings are now included in the array output
```

### Expected behavior
- For objects: key-value pairs where either the key OR value is an empty string should be excluded from the output
- For arrays: empty string elements should be filtered out from the array representation

The function should maintain deterministic output by excluding empty/invalid entries to ensure consistent serialization across different data structures.

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
