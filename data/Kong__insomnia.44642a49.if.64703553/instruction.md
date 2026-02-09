# Bug Report

### Describe the bug

I'm encountering an issue with URL parsing when trying to create a `Url` object with authentication credentials. The parser is throwing an error for valid URLs that contain username and password in the standard format.

### Reproduction

```js
const url = new Url('http://user:pass@example.com/path');
```

This throws an error:
```
Error: new Url(): failed to parse auth in url http://user:pass@example.com/path
```

### Expected behavior

The URL should be parsed correctly and the auth credentials should be extracted:
- username: `user`
- password: `pass`

This is a standard URL format that should be supported. URLs with authentication in the format `protocol://username:password@host` are commonly used and should parse without errors.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
