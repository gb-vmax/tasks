# Bug Report

### Describe the bug

I'm experiencing an issue with the no_proxy rule matching functionality. When I configure a no_proxy rule with an IPv6 address, it doesn't seem to work correctly. The proxy is still being used even though the URL should match the no_proxy rule.

### Reproduction

```js
// Set no_proxy environment variable with IPv6 address
process.env.no_proxy = '[::1]:8080'

// Try to make a request to localhost IPv6
const url = 'http://[::1]:8080/api/test'

// Expected: Request bypasses proxy
// Actual: Proxy is still used
```

### Expected behavior

When a no_proxy rule contains an IPv6 address (which uses colons in the address format like `[::1]` or `[2001:db8::1]`), the URL matching should correctly parse the hostname and port. The request should bypass the proxy when the URL matches the no_proxy rule.

### Additional context

This seems to affect IPv6 addresses specifically since they contain multiple colons. Regular hostnames with ports work fine (e.g., `localhost:8080`), but IPv6 addresses like `[::1]:8080` or `[2001:db8::1]:3000` don't match properly.

---
Repository: /testbed
