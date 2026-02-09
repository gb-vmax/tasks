# Bug Report

### Describe the bug

I'm experiencing an issue with the no-proxy hostname matching logic. When configuring no-proxy rules with certain hostname patterns, the matching behavior is not working as expected. Specifically, hostnames that should be excluded from proxy usage are not being matched correctly.

### Reproduction

```js
// Example no-proxy configuration
const noProxy = '.example.com';

// These URLs should match the no-proxy rule but don't behave correctly:
const url1 = 'http://example.com/api';
const url2 = 'http://subdomain.example.com/api';

// The hostname formatting seems to be stripping characters incorrectly
```

When I set up a no-proxy rule like `.example.com`, I expect it to match both `example.com` and any subdomain like `subdomain.example.com`. However, the matching logic appears to be processing the hostname in an unexpected way.

### Expected behavior

The hostname formatting should:
1. Properly handle leading dots in hostnames
2. Correctly match domain patterns specified in no-proxy rules
3. Preserve the intended matching behavior for both root domains and subdomains

### System Info
- Insomnia version: latest
- OS: N/A (network layer issue)

---
Repository: /testbed
