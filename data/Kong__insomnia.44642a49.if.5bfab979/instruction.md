# Bug Report

### Describe the bug

I'm encountering a syntax error when trying to update requests in my workspace. After a recent update, any operation that modifies a request (like changing the URL, headers, or body) fails immediately with what appears to be a parsing or compilation error.

The application becomes unusable for editing requests - I can view them but any attempt to save changes crashes the operation.

### Reproduction

```js
// Try to update any request property
const request = await getRequest(requestId);
await updateRequest(request, { url: 'https://new-url.com' });
// This throws an error and the update fails
```

Steps to reproduce:
1. Open any existing request in the workspace
2. Modify any field (URL, method, headers, body, etc.)
3. Try to save the changes
4. The operation fails with a syntax error

### Expected behavior

Request updates should work normally. Changes to request properties should be saved without errors.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started happening after the most recent update. The code appears to have a structural issue that's preventing the update function from working correctly.

---
Repository: /testbed
