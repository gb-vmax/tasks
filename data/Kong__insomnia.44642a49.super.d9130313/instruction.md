# Bug Report

### Describe the bug

The authentication configuration in Insomnia SDK is breaking when initializing `RequestAuth` objects. The constructor appears to be incomplete or corrupted, causing the authentication system to fail entirely.

### Reproduction

```js
const auth = new RequestAuth({
  type: 'basic',
  basic: [
    { key: 'username', value: 'testuser' },
    { key: 'password', value: 'testpass' }
  ]
});
```

When trying to create any auth object, the initialization fails. This affects all authentication types including basic, bearer, oauth1, oauth2, apikey, etc.

### Expected behavior

The `RequestAuth` constructor should properly initialize and validate the authentication options. It should accept the auth configuration and set up the internal state correctly.

### Additional context

This seems to have broken recently. The constructor code looks like it was modified but not completed properly - there's function definitions inside the constructor which doesn't make sense. The original validation logic for checking valid auth types seems to have been removed or displaced.

This is blocking all authentication-related functionality in the SDK.

---
Repository: /testbed
