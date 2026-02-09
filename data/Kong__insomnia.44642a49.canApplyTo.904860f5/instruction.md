# Bug Report

### Describe the bug

When configuring client certificates with URL patterns, the certificate matching logic is inverted. Certificates are being applied to URLs that DON'T match the pattern, and NOT applied to URLs that DO match the pattern.

### Reproduction

```js
const cert = new Certificate({
  name: 'My Cert',
  matches: /^https:\/\/api\.example\.com/,
  // ... other cert options
});

// This returns false (should return true)
cert.canApplyTo('https://api.example.com/endpoint');

// This returns true (should return false)
cert.canApplyTo('https://other-domain.com/endpoint');
```

### Expected behavior

The `canApplyTo()` method should return `true` when the URL matches the certificate's pattern, and `false` when it doesn't match. Currently it's doing the opposite.

This makes it impossible to correctly scope certificates to specific domains/URLs - they end up being applied to every request EXCEPT the ones they're intended for.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
