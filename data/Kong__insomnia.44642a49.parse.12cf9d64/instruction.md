# Bug Report

### Describe the bug
When parsing query strings using `QueryParam.parse()`, the returned array contains incorrect values. The method seems to be returning the key twice instead of returning both the key and value from each query parameter.

### Reproduction
```js
const queryString = 'foo=bar&name=test&id=123';
const parsed = QueryParam.parse(queryString);

console.log(parsed);
// Expected: [{ key: 'foo', value: 'bar' }, { key: 'name', value: 'test' }, { key: 'id', value: '123' }]
// Actual: [{ key: 'f', value: 'o' }, { key: 'n', value: 'a' }, { key: 'i', value: 'd' }]
```

The values are being set incorrectly - it looks like it's treating the keys as an array and using character indices instead of properly extracting the key-value pairs from the query string.

### Expected behavior
`QueryParam.parse()` should return an array of objects where each object has the correct `key` and `value` properties corresponding to the query parameters in the input string.

### System Info
- Package: insomnia-sdk
- Affected module: `packages/insomnia-sdk/src/objects/urls.ts`

---
Repository: /testbed
