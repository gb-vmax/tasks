# Bug Report

### Describe the bug

The `Header.parse()` method is not correctly parsing multi-line header strings. When I try to parse a string containing multiple headers separated by newlines, it returns an empty array instead of the expected array of header objects.

### Reproduction

```js
const headerString = 'Content-Type: application/json\nUser-Agent: MyClientLibrary/2.0\n';
const parsed = Header.parse(headerString);

console.log(parsed);
// Expected: [
//   { key: 'Content-Type', value: 'application/json' },
//   { key: 'User-Agent', value: 'MyClientLibrary/2.0' }
// ]
// Actual: []
```

### Expected behavior

The method should split the header string by newlines and parse each individual header into an object with `key` and `value` properties. Non-empty lines should be processed and empty lines should be filtered out.

### Additional context

This seems to affect any multi-line header string parsing. Single header parsing with `parseSingle()` appears to work fine, but when using `parse()` with multiple headers, nothing gets returned.

---
Repository: /testbed
