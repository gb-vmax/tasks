# Bug Report

### Describe the bug

I'm experiencing an issue with the no_proxy rule matching when using IPv6 addresses. When I specify an IPv6 address in the no_proxy configuration, the proxy bypass doesn't work correctly.

### Reproduction

```js
// Set no_proxy with an IPv6 address
const noProxy = '[2001:db8::1]:8080';

// Try to match a request to that IPv6 address
const url = 'http://[2001:db8::1]:8080/api';

// The URL should match the no_proxy rule but it doesn't
```

The problem seems to be with how IPv6 addresses with ports are parsed. IPv6 addresses contain colons (like `2001:db8::1`) and when you add a port, they need to be wrapped in brackets like `[2001:db8::1]:8080`. 

### Expected behavior

URLs with IPv6 addresses should correctly match against no_proxy rules that include IPv6 addresses with ports. The parser should handle the bracket notation and multiple colons in IPv6 addresses properly.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
