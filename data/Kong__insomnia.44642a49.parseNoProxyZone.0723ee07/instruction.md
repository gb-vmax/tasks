# Bug Report

### Describe the bug
When using the no_proxy configuration with IPv6 addresses, the proxy bypass rules are not working correctly. IPv6 addresses in no_proxy settings are being parsed incorrectly, causing requests that should bypass the proxy to still go through it.

### Reproduction
```js
// Set no_proxy with an IPv6 address
const noProxy = '[::1]:8080';

// Try to make a request to localhost IPv6
// Expected: Request bypasses proxy
// Actual: Request still goes through proxy
```

The issue appears when using IPv6 addresses with brackets in the no_proxy configuration. The hostname parsing doesn't handle the colons in IPv6 addresses properly.

### Expected behavior
Requests to IPv6 addresses listed in no_proxy should bypass the proxy server, just like IPv4 addresses and hostnames do.

### System Info
- Insomnia version: latest
- OS: All platforms

---
Repository: /testbed
