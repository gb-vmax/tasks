# Bug Report

### Describe the bug
API Key authentication with query parameters is not working correctly. When I configure an API key to be added as a query parameter, it's not being included in the request URL at all.

### Reproduction
```js
const authentication = {
  type: 'apikey',
  addTo: 'queryParams',
  key: 'api_key',
  value: 'my-secret-key-123'
}

// Expected: Query param should be added as ?api_key=my-secret-key-123
// Actual: No query parameter is added to the request
```

### Steps to reproduce:
1. Create a new request
2. Set authentication type to "API Key"
3. Configure it to add the key to "Query Params"
4. Set key name (e.g., "api_key") and value (e.g., "my-secret-key-123")
5. Send the request
6. The API key is not added to the URL query string

### Expected behavior
The API key should be appended to the request URL as a query parameter with the correct key-value pair.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking my workflow as I can't authenticate with APIs that require API keys in query parameters. Any help would be appreciated!

---
Repository: /testbed
