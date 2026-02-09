# Bug Report

### Describe the bug

I'm experiencing an issue with the `RequestAuth.use()` method where it's rejecting valid authentication types and allowing invalid ones. The validation logic appears to be inverted - when I pass a valid auth type like `'basic'` or `'bearer'`, it throws an error saying the type is invalid. Conversely, if I pass an invalid type, the method accepts it without any error.

### Reproduction

```js
const auth = new RequestAuth();

// This throws an error but shouldn't
auth.use('basic', { username: 'user', password: 'pass' });
// Error: invalid type (basic), it must be noauth | basic | bearer | jwt | digest | oauth1 | oauth2 | hawk | awsv4 | ntlm | apikey | edgegrid | asap.

// This also throws an error
auth.use('bearer', { token: 'my-token' });
// Error: invalid type (bearer), it must be noauth | basic | bearer | jwt | digest | oauth1 | oauth2 | hawk | awsv4 | ntlm | apikey | edgegrid | asap.

// But passing an invalid type doesn't throw any error (it should!)
auth.use('invalid-auth-type', {});
// No error thrown
```

### Expected behavior

The method should accept valid authentication types (basic, bearer, jwt, etc.) without throwing an error, and should throw an error when an invalid type is provided.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
