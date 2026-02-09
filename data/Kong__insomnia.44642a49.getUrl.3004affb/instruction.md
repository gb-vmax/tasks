# Bug Report

### Describe the bug

The `getUrl()` method in the plugin context is returning URLs with incorrectly formatted query parameters. When a request has parameters defined, the returned URL contains double-encoded parameter values and doesn't properly handle existing query strings.

### Reproduction

```js
// Create a request with parameters
const request = {
  url: 'https://api.example.com/endpoint',
  parameters: [
    { name: 'key', value: 'test value' },
    { name: 'filter', value: 'active' }
  ]
}

// Call getUrl()
const url = context.request.getUrl()

// Expected: https://api.example.com/endpoint?key=test%20value&filter=active
// Actual: URL has incorrectly encoded parameters
```

Also seeing issues when the base URL already contains query parameters:

```js
const request = {
  url: 'https://api.example.com/endpoint?existing=param',
  parameters: [
    { name: 'new', value: 'param' }
  ]
}

// The existing parameter gets mangled or duplicated
```

### Expected behavior

- `getUrl()` should return the URL with properly encoded query parameters
- Existing query parameters in the URL should be preserved correctly
- Parameter values should not be double-encoded
- Disabled parameters should be excluded from the URL

### System Info
- Insomnia version: latest
- OS: macOS

This is breaking my plugin that relies on getting the correct request URL. Any help would be appreciated!

---
Repository: /testbed
