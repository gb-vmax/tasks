# Bug Report

### Describe the bug

The proxy configuration resolution is not working correctly. When I have multiple proxy configs that match the same URL, the wrong proxy is being selected. It seems like the matching logic isn't properly prioritizing more specific patterns over general ones.

### Reproduction

```js
const proxyList = new ProxyConfigList();

// Add a specific proxy for api.example.com
proxyList.add({
  match: 'https://api.example.com/v1/*',
  host: 'specific-proxy.local',
  port: 8080
});

// Add a general wildcard proxy
proxyList.add({
  match: 'https://*.example.com/*',
  host: 'general-proxy.local',
  port: 9090
});

// Try to resolve a URL that matches both patterns
const resolved = proxyList.resolve(new Url('https://api.example.com/v1/users'));

// Expected: should return the more specific proxy (specific-proxy.local:8080)
// Actual: returns the wrong proxy or doesn't prioritize correctly
```

### Expected behavior

When multiple proxy configurations match a URL, the most specific pattern should be selected. More specific patterns (with fewer wildcards, more path segments, exact paths) should take priority over general wildcard patterns.

For example:
- `https://api.example.com/v1/users` should match `https://api.example.com/v1/*` over `https://*.example.com/*`
- Patterns with exact paths should be preferred over patterns ending with wildcards

### System Info
- insomnia-sdk version: latest
- The proxy resolution seems to be picking matches in an unpredictable order

---
Repository: /testbed
