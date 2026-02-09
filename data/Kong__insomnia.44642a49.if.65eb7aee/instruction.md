# Bug Report

### Describe the bug

I'm experiencing an issue with proxy resolution where the URL matching logic seems to be returning incorrect proxy configurations. When I have multiple proxy rules configured, the wrong proxy is being selected for certain URLs.

### Reproduction

```js
const proxyList = new ProxyConfigList();

// Add multiple proxy configurations
proxyList.add({
  match: 'http://*',
  host: 'proxy1.example.com',
  port: 8080
});

proxyList.add({
  match: 'http://api.example.com/*',
  host: 'proxy2.example.com',
  port: 8081
});

// Try to resolve a URL
const url = new Url('http://api.example.com/v1/users');
const proxy = proxyList.resolve(url);

// Expected: proxy2.example.com (more specific match)
// Actual: Getting inconsistent results or wrong proxy
console.log(proxy);
```

### Expected behavior

The proxy resolution should return the most specific matching proxy configuration. In the example above, `http://api.example.com/*` is more specific than `http://*`, so it should be selected for URLs matching `api.example.com`.

### Additional context

This seems to have started happening recently. The proxy selection appears to be non-deterministic or based on some unexpected criteria. Sometimes the correct proxy is selected, other times a less specific one is used instead.

---
Repository: /testbed
