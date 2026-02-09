# Bug Report

### Describe the bug

I'm having an issue with certificate host validation - requests are failing when they should be passing. It looks like the URL matching logic is incorrectly rejecting valid certificate hosts.

### Reproduction

```js
// This should return true but returns false
urlMatchesCertHost('example.com', 'https://example.com:443', true)

// This should also work but doesn't
urlMatchesCertHost('*.example.com', 'https://api.example.com:443', true)
```

When I try to use a client certificate with a matching hostname, the connection fails even though the hostname and port should match. The validation seems to be rejecting valid matches.

### Expected behavior

When the certificate host matches the request URL (including wildcards), the function should return `true` and allow the connection to proceed. Currently it's returning `false` for what should be valid matches.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
