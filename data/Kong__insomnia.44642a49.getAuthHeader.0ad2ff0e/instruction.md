# Bug Report

### Describe the bug

Cookie authentication is not working correctly - the key and value are being set in the wrong order in the Cookie header. When using cookie-based authentication, the generated header has the value and key swapped.

### Reproduction

```js
// Set up authentication with cookie type
const authentication = {
  type: 'cookie',
  key: 'session_id',
  value: 'abc123xyz'
};

// Expected Cookie header: session_id=abc123xyz
// Actual Cookie header: abc123xyz=session_id
```

The cookie is being formatted as `value=key` instead of the standard `key=value` format, which causes authentication to fail on the server side.

### Expected behavior

The Cookie header should be formatted with the key first, then the value: `key=value`

For example, if key is `session_id` and value is `abc123xyz`, the header should be:
```
Cookie: session_id=abc123xyz
```

### Additional context

This is breaking authentication for any requests that rely on cookie-based auth. The server doesn't recognize the malformed cookie format and rejects the requests.

---
Repository: /testbed
