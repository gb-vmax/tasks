# Bug Report

### Describe the bug

When creating a `RequestAuth` object with a valid auth type, I'm getting an error saying the auth type is invalid. This seems to be backwards - valid types are being rejected while invalid types would presumably be accepted.

### Reproduction

```js
const auth = new RequestAuth({
  type: 'bearer', // or any other valid auth type
  bearer: [
    { key: 'token', value: 'my-token' }
  ]
});
```

This throws an error:
```
Error: invalid auth type bearer
```

### Expected behavior

The `RequestAuth` constructor should accept valid auth types without throwing an error. Only invalid auth types should trigger the error message.

### System Info
- Package: insomnia-sdk
- Using bearer, basic, or other standard auth types

---
Repository: /testbed
