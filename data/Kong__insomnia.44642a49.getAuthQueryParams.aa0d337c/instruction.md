# Bug Report

### Describe the bug

API Key authentication is not being added to query parameters correctly. When I configure an API key with `addTo: 'query'`, the key-value pair is not appearing in the request URL query string.

### Reproduction

```js
const authentication = {
  type: 'apikey',
  addTo: 'query',
  key: 'api_key',
  value: 'my-secret-key'
}

const queryParams = getAuthQueryParams(authentication)
// Expected: { name: 'api_key', value: 'my-secret-key' }
// Actual: undefined
```

### Expected behavior

When API key authentication is configured with `addTo: 'query'`, the `getAuthQueryParams()` function should return an object with the key-value pair so it can be appended to the request URL as a query parameter.

### Additional context

This seems to have broken recently. API keys configured to be sent in headers still work fine, but query parameter authentication is completely non-functional. The request goes out without the API key, causing authentication failures on the server side.

---
Repository: /testbed
