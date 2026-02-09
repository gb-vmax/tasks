# Bug Report

### Describe the bug

I'm experiencing an issue with API key authentication when the authentication is enabled. It seems like the query parameters are not being added correctly to the request.

### Reproduction

```js
const authentication = {
  type: 'apikey',
  addTo: 'query',
  disabled: false,
  key: 'api_key',
  value: 'my-secret-key'
}

const queryParams = getAuthQueryParams(authentication);
// queryParams is undefined, but should contain the key/value pair
```

### Expected behavior

When authentication is **enabled** (disabled: false) and configured to add API key to query parameters, the `getAuthQueryParams` function should return an object with the key/value pair. Currently it returns undefined.

Also, it seems like the function is adding query params even when the `addTo` property is NOT set to query params, which doesn't make sense.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
