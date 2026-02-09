# Bug Report

### Describe the bug

I'm unable to create a new client certificate without specifying a `parentId`. The application throws an error saying "New ClientCertificate missing `parentId`" even when I'm providing the `parentId` in the configuration.

### Reproduction

```js
// This throws an error even though parentId is provided
const cert = create({
  parentId: 'workspace_123',
  host: 'example.com',
  cert: certData,
  key: keyData
});

// Error: New ClientCertificate missing `parentId`: {"parentId":"workspace_123","host":"example.com",...}
```

The error message is confusing because it claims the `parentId` is missing when it's clearly present in the object.

### Expected behavior

Creating a client certificate with a valid `parentId` should work without throwing an error. The validation should only fail when `parentId` is actually missing or undefined.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
