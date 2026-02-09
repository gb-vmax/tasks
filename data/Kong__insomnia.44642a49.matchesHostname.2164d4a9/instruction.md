# Bug Report

### Describe the bug

I'm experiencing an issue with the no_proxy wildcard matching functionality. When I configure a no_proxy rule with a wildcard pattern like `.*example.com`, it's not matching URLs correctly. It seems like the wildcard matching logic has changed and is now only matching if the pattern appears at the start of the hostname instead of at the end.

### Reproduction

```js
// Set up no_proxy with wildcard pattern
const noProxyRule = '.*example.com';

// Try to match against a subdomain
const url1 = 'https://api.example.com/endpoint';
const url2 = 'https://test.example.com/path';

// These should match the wildcard pattern but don't seem to be working as expected
```

When I use a wildcard pattern like `.*example.com`, I expect it to match any subdomain of `example.com` (like `api.example.com`, `test.example.com`, etc.). However, the matching behavior seems incorrect - it's checking if the pattern starts at position 0 of the hostname rather than checking if it ends with the pattern.

### Expected behavior

Wildcard patterns in no_proxy rules should match hostnames that end with the specified pattern. For example:
- `.*example.com` should match `api.example.com`, `test.example.com`, etc.
- The pattern should match at the end of the hostname, not just at the beginning

### Additional context

This affects proxy bypass configuration when using wildcard domains. The current behavior makes it difficult to properly configure no_proxy rules for entire domain hierarchies.

---
Repository: /testbed
