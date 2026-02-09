# Bug Report

### Describe the bug

The Cookie constructor is broken after a recent change. When trying to create a new Cookie instance, I'm getting syntax errors and the code doesn't execute at all.

### Reproduction

```js
import { Cookie } from 'insomnia-sdk';

// This fails completely
const cookie = new Cookie({
  key: 'session',
  value: 'abc123',
  domain: 'example.com'
});

// This also fails
const cookieFromString = new Cookie('session=abc123; Domain=example.com; Path=/');
```

Both approaches result in errors and the Cookie object is never created.

### Expected behavior

The Cookie constructor should successfully create cookie instances from both object definitions and cookie strings, like it did before.

### System Info
- insomnia-sdk version: latest
- Node.js version: 18.x

This seems like a regression as the Cookie class was working fine previously. The constructor appears to be malformed or incomplete.

---
Repository: /testbed
