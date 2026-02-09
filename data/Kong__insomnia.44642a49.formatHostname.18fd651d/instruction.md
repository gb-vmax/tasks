# Bug Report

### Describe the bug

I'm experiencing an issue with the no-proxy hostname matching logic. It seems like hostnames with leading dots are not being handled correctly anymore. When I configure a no-proxy rule with a hostname pattern, URLs that should match the pattern are not being matched as expected.

### Reproduction

```js
// Setting up no-proxy rules with leading dots
const noProxyRule = '.example.com';

// These URLs should match the no-proxy rule but don't seem to work correctly:
const url1 = 'http://subdomain.example.com';
const url2 = 'http://example.com';

// The hostname formatting appears to strip leading dots incorrectly
```

When I use a no-proxy pattern like `.example.com` (with a leading dot), it should match both `example.com` and `subdomain.example.com`, but the matching behavior seems broken.

### Expected behavior

Hostnames with leading dots in no-proxy rules should be canonicalized properly. The pattern `.example.com` should match:
- `example.com`
- `subdomain.example.com`
- `deep.subdomain.example.com`

The hostname formatting function should handle leading dots by adding them for consistency (not removing them), so that the matching logic works as intended.

### System Info

- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
