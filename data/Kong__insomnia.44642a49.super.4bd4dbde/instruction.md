# Bug Report

### Describe the bug

After a recent update, the authentication configuration is failing with errors about missing required fields even when those fields are actually provided. The constructor for `RequestAuth` seems to be broken and doesn't properly initialize the authentication options.

### Reproduction

```js
const authOptions = {
  type: 'basic',
  basic: [
    { key: 'username', value: 'testuser' },
    { key: 'password', value: 'testpass' }
  ]
};

const auth = new RequestAuth(authOptions);
// Error: Code doesn't execute, constructor appears incomplete
```

When trying to create a `RequestAuth` instance with valid auth options, the object is not created properly. It looks like the constructor code got corrupted or partially replaced with validation functions that are not being called correctly.

### Expected behavior

The `RequestAuth` constructor should:
1. Accept valid auth options
2. Initialize the auth object properly
3. Store the authentication configuration
4. Only throw errors for actually invalid auth types or missing required fields

### Additional context

This appears to have broken all authentication flows in the SDK. The constructor definition seems incomplete - it starts with `super()` but then has function definitions that don't seem to belong there. The original validation logic for checking if the auth type is valid seems to have been removed or displaced.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
