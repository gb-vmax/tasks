# Bug Report

### Describe the bug

When using `Header.unparse()` to convert headers back to string format, the method throws an error. It appears that the unparsing logic is trying to spread a string into an array incorrectly.

### Reproduction

```js
const headers = [
  { key: 'Content-Type', value: 'application/json' },
  { key: 'User-Agent', value: 'MyClientLibrary/2.0' }
];

// This throws an error
const headerString = Header.unparse(headers);
```

### Expected behavior

The `unparse()` method should convert the array of header objects back into a properly formatted header string like:
```
Content-Type: application/json
User-Agent: MyClientLibrary/2.0
```

Instead, it's failing during the conversion process.

### Additional context

This seems to have broken recently. The unparsing functionality was working fine before.

---
Repository: /testbed
