# Bug Report

### Describe the bug

I'm encountering an issue where creating a `RequestAuth` object with a valid auth type throws an error, while invalid auth types are accepted without any validation. This seems like the validation logic is inverted.

### Reproduction

```js
// This throws an error but shouldn't
const auth = new RequestAuth({
  type: 'bearer'  // valid auth type
});
// Error: invalid auth type bearer

// This should throw an error but doesn't
const invalidAuth = new RequestAuth({
  type: 'invalid_type'  // invalid auth type
});
// No error thrown
```

### Expected behavior

Valid auth types like 'bearer', 'basic', 'oauth2', etc. should be accepted without throwing an error. Invalid auth types should throw an error with the message "invalid auth type {type}".

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
