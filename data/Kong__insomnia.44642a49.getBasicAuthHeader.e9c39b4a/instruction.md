# Bug Report

### Describe the bug
Basic authentication headers are being generated incorrectly. The username and password are being reversed in the authorization header, which causes authentication to fail when making requests.

### Reproduction
```js
import { getBasicAuthHeader } from './network/basic-auth/get-header';

const header = getBasicAuthHeader('myuser', 'mypass');
console.log(header);

// The Authorization header value is encoded with password:username
// instead of the correct username:password format
```

### Expected behavior
The Basic Auth header should follow the standard format of `username:password` encoded in base64. Currently it appears to be encoding `password:username` instead, which breaks authentication with any service expecting proper Basic Auth credentials.

### System Info
- Insomnia version: latest
- OS: macOS

This is causing all my API requests with basic auth to fail. Would appreciate a fix for this!

---
Repository: /testbed
