# Bug Report

### Describe the bug

When parsing query strings using `QueryParam.parse()`, the key-value pairs are being returned incorrectly. The keys and values appear to be swapped, and the first parameter in the query string is missing from the results.

### Reproduction

```js
const queryString = 'foo=bar&name=test&id=123';
const params = QueryParam.parse(queryString);

console.log(params);
// Expected: [{ key: 'foo', value: 'bar' }, { key: 'name', value: 'test' }, { key: 'id', value: '123' }]
// Actual: [{ key: 'test', value: 'name' }, { key: '123', value: 'id' }]
```

The first parameter (`foo=bar`) is completely missing, and the remaining parameters have their keys and values reversed.

### Expected behavior

`QueryParam.parse()` should return an array with all query parameters where:
- Each object has the correct `key` property matching the parameter name
- Each object has the correct `value` property matching the parameter value
- All parameters from the query string are included in the result

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
