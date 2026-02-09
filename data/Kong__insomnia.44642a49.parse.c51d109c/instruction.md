# Bug Report

### Describe the bug

The `QueryParam.parse()` method is not correctly handling query strings anymore. After a recent update, the parsed query parameters are returning objects with unexpected properties that break existing code expecting the original simple `{key, value}` format.

### Reproduction

```js
const queryStr = 'foo=bar&baz=123';
const params = QueryParam.parse(queryStr);

console.log(params);
// Expected: [{ key: 'foo', value: 'bar' }, { key: 'baz', value: '123' }]
// Actual: [{ key: 'foo', value: 'bar', type: 'text' }, { key: 'baz', value: '123', type: 'number' }]
```

The parsed result now includes an additional `type` property that wasn't there before. This is causing issues in our application where we iterate over the params and only expect `key` and `value` properties.

### Steps to reproduce

1. Parse a query string using `QueryParam.parse()`
2. Check the returned array structure
3. Notice the extra `type` field in each param object

### Expected behavior

The method should return an array of objects with only `key` and `value` properties, matching the previous behavior. Any additional metadata should be opt-in or handled in a backwards-compatible way.

### Additional context

This appears to have changed recently and is breaking our existing integrations that rely on the simpler object structure. Not sure if this was intentional or an accidental breaking change.

---
Repository: /testbed
