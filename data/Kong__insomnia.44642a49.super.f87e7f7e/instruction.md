# Bug Report

### Describe the bug
I'm unable to create Cookie objects from cookie strings anymore. Every time I try to parse a valid cookie string, I get an error saying "failed to parse cookie, the cookie string seems invalid" even though the cookie string is perfectly valid.

### Reproduction
```js
const sdk = require('insomnia-sdk');

// This throws an error even though it's a valid cookie string
const cookie = new sdk.Cookie('sessionId=abc123; Path=/; HttpOnly');
```

The error message I get is:
```
Error: failed to parse cookie, the cookie string seems invalid
```

### Expected behavior
The Cookie constructor should accept valid cookie strings and parse them correctly without throwing errors. This used to work in previous versions.

### Additional context
This seems to have started happening recently. I can't create cookies from strings at all now, which breaks a lot of my existing code that relies on parsing cookie strings.

---
Repository: /testbed
