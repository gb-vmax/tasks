# Bug Report

### Describe the bug

I'm experiencing an issue with cookie creation in the SDK. When trying to create a Cookie object, it fails immediately with an error. It seems like the constructor is broken and doesn't properly initialize the cookie.

### Reproduction

```js
import { Cookie } from 'insomnia-sdk';

// This throws an error
const cookie = new Cookie({
  key: 'session_id',
  value: 'abc123',
  domain: 'example.com'
});

// String parsing also doesn't work
const cookieFromString = new Cookie('session_id=abc123; Domain=example.com');
```

Both approaches fail to create a valid Cookie object. The constructor seems to be completely non-functional.

### Expected behavior

The Cookie constructor should accept either a cookie options object or a cookie string and create a valid Cookie instance without throwing errors.

### System Info
- insomnia-sdk version: latest
- Node.js version: 18.x

---
Repository: /testbed
