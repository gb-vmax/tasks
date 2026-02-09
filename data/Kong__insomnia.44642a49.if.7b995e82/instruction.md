# Bug Report

### Describe the bug

When parsing URLs with authentication credentials, the password field is not being set correctly. Instead of getting the actual password from the auth string, it appears to be using the username value for both fields.

### Reproduction

```js
const url = new Url('https://user:pass@example.com/path');
console.log(url.auth.username); // Expected: 'user'
console.log(url.auth.password); // Expected: 'pass', but getting 'user'
```

The auth object ends up with the same value for both username and password properties, which breaks authentication when making requests with credentials.

### Expected behavior

When parsing a URL like `https://username:password@host.com`, the auth object should correctly extract:
- `username` → 'username'
- `password` → 'password'

Currently both fields are being set to the username value.

### Additional context

This affects any URL that includes authentication credentials in the format `protocol://user:pass@host`. The parsing logic seems to be extracting the auth string correctly but not splitting it properly into username and password components.

---
Repository: /testbed
