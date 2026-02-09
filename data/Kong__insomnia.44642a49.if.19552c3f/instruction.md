# Bug Report

### Describe the bug

After a recent update, OAuth2 authentication is not working properly when accessing configuration values. The function appears to have duplicate code that's causing the logic to break - there's a nested function definition followed by duplicate code that tries to do the same thing.

### Reproduction

When trying to use OAuth2 authentication with configuration options:

```js
const auth = {
  type: 'oauth2',
  options: [
    { key: 'accessToken', value: 'my-token' },
    { key: 'clientId', value: 'my-client-id' }
  ]
};

// The authentication fails to retrieve values correctly
// Expected to get 'my-token' but returns empty string or undefined
```

### Expected behavior

The OAuth2 authentication should correctly retrieve configuration values from the options array. The function should process the key-value pairs and return the matching value for a given key.

### Additional context

Looking at the code, it seems like there's a malformed function definition that's creating duplicate logic. The `findValueInOauth2Options` function is defined inside the loop but then the same matching logic appears again right after it, which would cause the function to never actually be called or used properly.

This is breaking OAuth2 authentication flows that rely on retrieving configuration values from the auth options.

---
Repository: /testbed
