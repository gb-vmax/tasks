# Bug Report

### Describe the bug

I'm encountering an issue where creating a `RequestAuth` object with a valid auth type throws an error saying "valid auth type", which doesn't make sense. It seems like the validation logic is inverted - valid auth types are being rejected instead of invalid ones.

### Reproduction

```js
const auth = new RequestAuth({
  type: 'bearer',  // or any other valid auth type
  bearer: [
    { key: 'token', value: 'my-token' }
  ]
});
```

This throws an error: `Error: valid auth type bearer`

### Expected behavior

The `RequestAuth` constructor should accept valid auth types without throwing an error. It should only throw an error when an *invalid* auth type is provided, not when a valid one is used.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
