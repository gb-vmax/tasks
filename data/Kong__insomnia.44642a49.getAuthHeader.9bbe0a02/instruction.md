# Bug Report

### Describe the bug

When using API Key authentication with the "Add To" option set to Cookie, the authentication header is being set incorrectly. Instead of adding the API key to the Cookie header, it's being added to the Authorization header.

### Reproduction

1. Create a new request
2. Set authentication type to "API Key"
3. Set "Add To" dropdown to "Cookie"
4. Enter a key name (e.g., "session_id") and value (e.g., "abc123")
5. Send the request

### Expected behavior

The API key should be sent in the Cookie header:
```
Cookie: session_id=abc123
```

### Actual behavior

The API key is being sent in the Authorization header instead:
```
Authorization: session_id=abc123
```

This breaks authentication for APIs that expect the API key to be in a cookie rather than the Authorization header.

### System Info
- Insomnia version: latest
- OS: Windows 10

---
Repository: /testbed
