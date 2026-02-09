# Bug Report

### Describe the bug
When using wildcard patterns in no_proxy rules, URLs are not being matched correctly. Specifically, patterns starting with `*.*` don't work as expected, and hostname matching fails for certain valid cases.

### Reproduction
```js
// Example 1: Wildcard pattern not matching
const noProxyRule = '*.example.com';
const url = 'https://api.example.com';
// Expected: Should match and bypass proxy
// Actual: Does not match

// Example 2: Hostname matching issue
const noProxyRule = '.example.com';
const url = 'https://sub.example.com';
// Expected: Should match
// Actual: Matching behavior is inconsistent
```

### Expected behavior
- Wildcard patterns like `*.example.com` should correctly match subdomains
- Hostname matching should work for all valid subdomain patterns
- The no_proxy rule matching should be consistent with standard proxy bypass behavior

### System Info
- Insomnia version: latest
- OS: Any

This is affecting our ability to properly configure proxy bypass rules for internal domains.

---
Repository: /testbed
