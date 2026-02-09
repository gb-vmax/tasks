# Bug Report

### Describe the bug

When calling `request.auth.use()` with a valid authentication type, an error is thrown saying the type is invalid. The error message claims valid types like `'basic'`, `'bearer'`, `'oauth1'`, etc. are not valid, which prevents setting up authentication for requests.

### Reproduction

```js
const request = new Request('https://api.example.com');

// This throws an error even though 'basic' is a valid type
request.auth.use('basic', {
  username: 'user',
  password: 'pass'
});

// Error: invalid type (basic), it must be noauth | basic | bearer | jwt | digest | oauth1 | oauth2 | hawk | awsv4 | ntlm | apikey | edgegrid | asap.
```

The same issue occurs with other valid authentication types like `'bearer'`, `'oauth1'`, etc.

### Expected behavior

The `use()` method should accept valid authentication types without throwing an error. It should only throw an error when an actually invalid type is provided (like `'invalid-type'` or `'xyz'`).

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
