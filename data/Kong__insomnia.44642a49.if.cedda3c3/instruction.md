# Bug Report

### Describe the bug

After a recent update, proxy resolution is returning incorrect results when the proxy configuration list is modified. When I add, remove, or clear proxy configs, subsequent URL resolutions still return stale proxy configurations that should no longer match.

### Reproduction

```js
const proxyList = new ProxyConfigList();

// Add initial proxy config
proxyList.add({
  match: 'http://example.com/*',
  host: 'proxy1.local',
  port: 8080
});

// Resolve URL - works correctly
const result1 = proxyList.resolve(new Url('http://example.com/api'));
console.log(result1.host); // proxy1.local

// Clear all proxies
proxyList.clear();

// Resolve same URL again - should return null but returns old proxy
const result2 = proxyList.resolve(new Url('http://example.com/api'));
console.log(result2); // Expected: null, Actual: { host: 'proxy1.local', port: 8080 }
```

Similar issue occurs when using `remove()` or `insert()` - the proxy resolution doesn't reflect the updated configuration list.

### Expected behavior

When proxy configurations are modified (cleared, removed, or new ones inserted), the `resolve()` method should return results based on the current state of the proxy list, not cached/stale values.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
