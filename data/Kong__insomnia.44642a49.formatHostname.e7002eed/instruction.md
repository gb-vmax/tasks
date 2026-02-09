# Bug Report

### Describe the bug

The `no_proxy` rule matching is not working correctly for certain hostname patterns. When using hostnames with leading dots in the no_proxy configuration, the matching behavior is inconsistent and doesn't properly handle domain wildcards.

### Reproduction

```js
// Configure no_proxy with a leading dot pattern
const noProxy = '.example.com';

// Try to match against a subdomain
const url = 'https://api.example.com/endpoint';

// The hostname matching fails when it should succeed
// Expected: URL should be matched by the no_proxy rule
// Actual: URL is not matched
```

### Expected behavior

Hostnames with leading dots in no_proxy rules should be properly canonicalized and matched against URLs. For example:
- `.example.com` should match `api.example.com`, `www.example.com`, etc.
- The hostname formatting should consistently handle leading dots

### System Info
- Insomnia version: latest
- OS: All platforms

This seems to have started happening recently and is affecting proxy bypass configurations.

---
Repository: /testbed
