# Bug Report

### Describe the bug

When creating a `Cookie` object from a string, the constructor is broken and doesn't work at all. It looks like some code got mangled or corrupted during a recent change - the constructor has static method definitions inside it and the actual constructor logic is incomplete.

### Reproduction

```js
const { Cookie } = require('insomnia-sdk');

// This throws an error or fails to create a proper cookie
const cookie = new Cookie('sessionId=abc123; Path=/; HttpOnly');
```

Trying to create any cookie from a string fails because the constructor code is malformed. The static validation methods are defined in the middle of the constructor body, and the actual parsing/initialization logic appears to be cut off.

### Expected behavior

Should be able to create a Cookie object from a valid cookie string without errors. The constructor should properly parse the cookie string and initialize the cookie properties.

### System Info
- insomnia-sdk: latest
- Node.js: v18.x

This is blocking our ability to work with cookies in the SDK. Any cookie creation from strings is currently broken.

---
Repository: /testbed
