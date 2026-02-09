# Bug Report

### Describe the bug

The no_proxy rule matching is not working correctly for CIDR notation and wildcard patterns. When I specify IP ranges using CIDR notation (e.g., `192.168.1.0/24`) or use wildcard patterns (e.g., `*.example.com`), the proxy bypass rules are not being applied as expected.

### Reproduction

```js
// CIDR notation example
// Setting no_proxy to: 192.168.1.0/24
// Trying to access: http://192.168.1.50
// Expected: Should bypass proxy
// Actual: Still uses proxy

// Wildcard pattern example  
// Setting no_proxy to: *.internal.company.com
// Trying to access: http://api.internal.company.com
// Expected: Should bypass proxy
// Actual: Still uses proxy
```

The current implementation only seems to handle the basic `.*.` prefix pattern but doesn't support:
1. CIDR notation for IP ranges (e.g., `10.0.0.0/8`, `192.168.0.0/16`)
2. Wildcard patterns that don't start with `.*.` (e.g., `*.example.com`, `test-*.local`)

### Expected behavior

- CIDR notation should match any IP address within the specified range
- Wildcard patterns with `*` should match multiple hostnames according to the pattern
- For example, `*.example.com` should match `api.example.com`, `www.example.com`, etc.
- `192.168.1.0/24` should match any IP from `192.168.1.0` to `192.168.1.255`

### System Info
- Insomnia version: latest
- OS: Cross-platform issue

This is blocking our ability to properly configure proxy bypass rules for internal networks and development environments.

---
Repository: /testbed
