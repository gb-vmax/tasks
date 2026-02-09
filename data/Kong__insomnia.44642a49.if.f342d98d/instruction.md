# Bug Report

### Describe the bug
When trying to set authentication type using the `use()` method with valid auth types, I'm getting an error saying the type is invalid. It seems like the validation logic is inverted - valid types are being rejected instead of accepted.

### Reproduction
```js
const auth = new RequestAuth();

// This throws an error but shouldn't
auth.use('basic', {
  username: 'test',
  password: 'pass'
});

// Error: invalid type (basic), it must be noauth | basic | bearer | jwt | digest | oauth1 | oauth2 | hawk | awsv4 | ntlm | apikey | edgegrid.
```

The same issue occurs with any valid auth type like 'bearer', 'oauth1', 'oauth2', etc. All valid authentication types are being rejected.

### Expected behavior
The `use()` method should accept valid authentication types without throwing an error. Only invalid/unsupported types should trigger the error message.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
