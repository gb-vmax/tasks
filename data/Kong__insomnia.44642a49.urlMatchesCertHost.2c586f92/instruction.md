# Bug Report

### Describe the bug

When using wildcard patterns in certificate host configuration, the matching logic appears to be inverted. Specifically, when a certificate host contains a wildcard in the port (e.g., `example.com:*`), URLs that should match are being rejected, and vice versa.

### Reproduction

```js
// This should return true but returns false
urlMatchesCertHost('example.com:*', 'https://example.com:8080', true)

// This should return false but returns true
urlMatchesCertHost('example.com:808*', 'https://example.com:9090', true)
```

The wildcard port matching seems to be backwards - it's returning false when the pattern matches and true when it doesn't match.

### Expected behavior

When a certificate host is configured with a wildcard port pattern (like `example.com:*` or `example.com:808*`), it should:
- Return `true` for URLs where the port matches the pattern
- Return `false` for URLs where the port doesn't match the pattern

Currently it's doing the opposite.

### System Info
- Version: Latest
- OS: Cross-platform issue

---
Repository: /testbed
