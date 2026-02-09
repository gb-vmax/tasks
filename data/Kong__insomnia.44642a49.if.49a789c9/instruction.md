# Bug Report

### Describe the bug

I'm experiencing an issue with OAuth2 authentication where key lookups in the auth options are case-sensitive. When the key casing doesn't match exactly, the authentication fails to retrieve the correct values.

### Reproduction

```js
const auth = {
  type: 'oauth2',
  grantType: 'authorization_code',
  // Keys with different casing
  accessTokenUrl: 'https://example.com/token',
  AccessTokenUrl: 'https://example.com/token', // This won't be found if looking for 'accesstokenurl'
}

// Trying to retrieve with different casing fails
// Expected to find the value regardless of case
```

### Expected behavior

OAuth2 authentication key lookups should be case-insensitive. Common OAuth2 parameters like `accessTokenUrl`, `clientId`, `clientSecret`, etc. should be retrievable regardless of whether they're provided as `AccessTokenUrl`, `ACCESSTOKENURL`, or any other casing variation.

This is particularly important since different OAuth2 providers and documentation use different casing conventions, and it's easy to accidentally use the wrong case when configuring authentication.

### System Info
- Insomnia SDK version: latest
- Node version: 18.x

---
Repository: /testbed
