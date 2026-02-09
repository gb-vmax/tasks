# Bug Report

### Describe the bug

I'm experiencing an issue with OAuth2 authentication where the parameter lookup is case-sensitive. When OAuth2 configuration parameters are passed with different casing (e.g., `AccessToken` vs `accesstoken`), they are not being recognized properly.

### Reproduction

```js
// OAuth2 configuration with mixed case keys
const auth = {
  type: 'oauth2',
  oauth2: [
    { key: 'AccessToken', value: 'my-token-123' },
    { key: 'RefreshToken', value: 'refresh-456' }
  ]
}

// Trying to retrieve with lowercase key
// Expected: should find 'AccessToken'
// Actual: returns empty string because case doesn't match
```

This is problematic because different OAuth2 providers and configurations use different casing conventions (camelCase, PascalCase, lowercase, etc.), and the current implementation requires exact case matching.

### Expected behavior

OAuth2 parameter lookup should be case-insensitive. Parameters like `accessToken`, `AccessToken`, and `ACCESSTOKEN` should all be treated as equivalent and return the same value.

### System Info
- Package: insomnia-sdk
- Affected module: auth.ts

---
Repository: /testbed
