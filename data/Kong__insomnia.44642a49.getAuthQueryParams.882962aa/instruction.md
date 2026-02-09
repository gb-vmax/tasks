# Bug Report

### Describe the bug
API key authentication is not being added to query parameters when configured to do so. Even though I've set `addTo` to query params in the authentication settings, the API key is not appearing in the request URL.

### Reproduction
```js
const authentication = {
  type: 'apikey',
  disabled: false,
  addTo: 'query', // or QUERY_PARAMS constant
  key: 'api_key',
  value: 'my-secret-key'
}

// Call getAuthQueryParams with this config
const queryParams = getAuthQueryParams(authentication);

// Expected: { name: 'api_key', value: 'my-secret-key' }
// Actual: undefined
```

### Expected behavior
When authentication is enabled and `addTo` is set to query params, the function should return an object with the key/value pair to be added as query parameters to the request URL.

### Additional context
This seems to have started recently. The authentication works fine when adding the API key to headers, but not when trying to add it to query parameters. Not sure if this is related to any recent changes in the authentication module.

---
Repository: /testbed
