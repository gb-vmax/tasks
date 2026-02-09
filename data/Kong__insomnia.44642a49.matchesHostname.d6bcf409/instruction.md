# Bug Report

### Describe the bug

I'm experiencing an issue with the no_proxy wildcard matching functionality. When using wildcard patterns like `*.example.com` in the no_proxy configuration, the matching behavior is incorrect. URLs that should be excluded from proxy are not being matched properly.

### Reproduction

When I set up a no_proxy rule with a wildcard pattern:

```
no_proxy: *.example.com
```

And then try to access URLs like:
- `https://api.example.com` - should match but doesn't work correctly
- `https://sub.example.com` - should match but doesn't work correctly
- `https://example.com` - behavior is unexpected

The wildcard matching seems to be broken. It looks like the pattern matching logic is not correctly handling the `*.` prefix.

### Expected behavior

When using `*.example.com` as a no_proxy rule:
- All subdomains of `example.com` should be matched and bypass the proxy
- The matching should work consistently across different subdomain levels

### System Info
- Insomnia version: latest
- OS: macOS

This is affecting our workflow where we need to bypass proxy for internal domains using wildcard patterns.

---
Repository: /testbed
