# Bug Report

### Describe the bug

I'm experiencing an issue with the no_proxy rule matching for wildcard hostnames. When I configure a no_proxy rule with a wildcard pattern like `*.example.com`, it doesn't match hostnames correctly. 

### Reproduction

When setting up a no_proxy rule with a wildcard pattern:

```
NO_PROXY=*.example.com
```

Expected matches:
- `api.example.com` - should match
- `test.example.com` - should match  
- `sub.domain.example.com` - should match

However, the wildcard matching doesn't seem to work as expected. The hostname matching logic appears to be too strict and may not be catching all the cases where a hostname should match the wildcard pattern.

### Expected behavior

Wildcard patterns in no_proxy rules should match any hostname that ends with the specified domain. For example, `*.example.com` should match `api.example.com`, `test.example.com`, and even `subdomain.api.example.com`.

### Additional context

This affects proxy bypass configuration and could cause requests that should bypass the proxy to incorrectly go through it, or vice versa.

---
Repository: /testbed
