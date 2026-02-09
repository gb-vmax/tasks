# Bug Report

### Describe the bug

When parsing query strings using `QueryParam.parse()`, the keys and values are being swapped. The method returns objects where the key contains the value and the value contains the key.

### Reproduction

```js
const queryStr = 'foo=bar&name=value';
const params = QueryParam.parse(queryStr);

// Expected: [{ key: 'foo', value: 'bar' }, { key: 'name', value: 'value' }]
// Actual: [{ key: 'bar', value: 'foo' }, { key: 'value', value: 'name' }]
```

### Expected behavior

The parsed query parameters should have the correct key-value mapping where `key` contains the parameter name and `value` contains the parameter value.

### Additional context

This appears to affect URL query string parsing in the SDK. Any code relying on `QueryParam.parse()` will receive inverted key-value pairs.

---
Repository: /testbed
