# Bug Report

### Describe the bug

After a recent update, OAuth2 authentication is not working properly when trying to access nested configuration values. The authentication flow fails silently and requests are sent without proper authorization headers.

### Reproduction

```js
const auth = {
  type: 'oauth2',
  grantType: 'authorization_code',
  accessTokenUrl: 'https://example.com/token',
  clientId: 'my-client-id',
  clientSecret: 'my-secret',
  // Nested configuration
  advancedOptions: [
    { key: 'audience', value: 'https://api.example.com' },
    { key: 'resource', value: 'https://resource.example.com' }
  ]
}

// When making a request with this auth config, the nested values are not being picked up
// The request goes through but without the expected authorization
```

### Expected behavior

The OAuth2 authentication should properly resolve nested configuration values and include them in the authorization flow. Requests should be sent with the correct authorization headers based on the complete configuration including nested options.

### Additional context

This seems to have started happening after some changes to the auth handling code. The basic OAuth2 flow works fine with flat configurations, but as soon as nested options are involved, they're not being processed correctly.

---
Repository: /testbed
