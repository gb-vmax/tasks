# Bug Report

### Describe the bug

When setting authentication type using the `use()` method, valid authentication types are being rejected with an error message saying they're invalid. The method is throwing an error for legitimate auth types like 'basic', 'bearer', 'oauth1', etc.

### Reproduction

```js
const auth = new RequestAuth();

// This throws an error even though 'basic' is a valid type
auth.use('basic', {
  username: 'testuser',
  password: 'testpass'
});

// Error: invalid type (basic), it must be noauth | basic | bearer | jwt | digest | oauth1 | oauth2 | hawk | awsv4 | ntlm | apikey | edgegrid | asap.
```

The same issue occurs with other valid auth types:
```js
auth.use('bearer', { token: 'abc123' }); // Also throws error
auth.use('oauth1', { /* options */ }); // Also throws error
```

### Expected behavior

The `use()` method should accept valid authentication types without throwing an error. Only invalid/unsupported auth types should trigger the error message.

### Additional context

This seems to have started happening recently. The error message itself lists the valid types, but those exact types are being rejected when passed to the method.

---
Repository: /testbed
