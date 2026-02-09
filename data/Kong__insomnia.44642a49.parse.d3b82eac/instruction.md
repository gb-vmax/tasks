# Bug Report

### Describe the bug

I'm experiencing an issue with query parameter parsing where the keys and values are being swapped. When I parse a query string, the parameter names end up as values and vice versa.

### Reproduction

```js
const queryString = 'foo=bar&name=john';
const params = QueryParam.parse(queryString);

console.log(params);
// Currently returns: [{ key: 'bar', value: 'foo' }, { key: 'john', value: 'name' }]
```

### Expected behavior

The parsed query parameters should maintain the correct key-value mapping:

```js
// Expected: [{ key: 'foo', value: 'bar' }, { key: 'name', value: 'john' }]
```

This is causing issues when trying to access query parameters in requests, as the keys and values are reversed.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
