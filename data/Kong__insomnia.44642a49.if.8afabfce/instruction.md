# Bug Report

### Describe the bug

After a recent update, OAuth2 authentication is failing with incomplete or malformed token requests. The authentication flow appears to break when trying to extract OAuth2 configuration values from the request authentication object.

### Reproduction

When setting up OAuth2 authentication with the following configuration:

```js
const auth = {
  type: 'oauth2',
  oauth2: [
    { key: 'clientId', value: 'my-client-id' },
    { key: 'clientSecret', value: 'my-secret' },
    { key: 'accessTokenUrl', value: 'https://example.com/token' }
  ]
};
```

The authentication process fails to properly read the configuration values. It seems like the code that extracts values from the OAuth2 options is broken or incomplete.

### Expected behavior

OAuth2 authentication should work correctly by extracting the necessary configuration values (clientId, clientSecret, accessTokenUrl, etc.) from the authentication object and using them to complete the token request flow.

### Additional context

This appears to have started happening after changes to the `fromPreRequestAuth` function in the auth module. The function seems to have been modified but the changes look incomplete - there's a new `findValueInOauth2Options` function defined but the original logic for iterating through key-value pairs appears to be cut off mid-implementation.

---
Repository: /testbed
