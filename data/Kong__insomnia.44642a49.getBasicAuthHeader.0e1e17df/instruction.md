# Bug Report

### Describe the bug
Basic authentication is not working correctly - the username and password appear to be swapped in the Authorization header. When I try to authenticate with valid credentials, I'm getting 401 Unauthorized responses from the server.

### Reproduction
```js
const username = 'myuser';
const password = 'mypass';
const header = getBasicAuthHeader(username, password);

// The resulting header has password:username instead of username:password
// This causes authentication to fail
```

### Expected behavior
The Basic Auth header should be formatted as `Basic base64(username:password)` according to RFC 7617. Currently it seems to be encoding the credentials in the wrong order.

### Steps to reproduce
1. Set up a request with Basic Authentication
2. Provide valid username and password
3. Send the request
4. Server returns 401 Unauthorized even though credentials are correct

This is breaking authentication for all my API requests that use Basic Auth. The credentials are definitely correct because they work in other tools like Postman.

---
Repository: /testbed
