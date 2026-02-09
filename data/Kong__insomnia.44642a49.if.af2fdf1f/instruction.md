# Bug Report

### Describe the bug

I'm experiencing an issue with proxy resolution where the same URL object is being resolved multiple times but returns stale/cached results even after the proxy configuration list has been modified.

### Reproduction

```js
const proxyList = new ProxyConfigList();

// Add a proxy config
proxyList.add({
  match: 'https://example.com/*',
  host: 'proxy1.com',
  port: 8080
});

const url = new Url('https://example.com/api');

// First resolution works correctly
const result1 = proxyList.resolve(url);
console.log(result1); // Returns proxy1.com:8080

// Disable the proxy
proxyList.list[0].disabled = true;

// Second resolution with same URL object returns cached result
const result2 = proxyList.resolve(url);
console.log(result2); // Still returns proxy1.com:8080 instead of null
```

### Expected behavior

When the proxy configuration list is modified (e.g., a proxy is disabled or removed), subsequent calls to `resolve()` should return updated results based on the current state of the list, not cached values from previous resolutions.

### Additional context

This seems to happen when reusing the same URL object for multiple resolution calls. The caching mechanism appears to not properly invalidate when the underlying proxy list changes.

---
Repository: /testbed
