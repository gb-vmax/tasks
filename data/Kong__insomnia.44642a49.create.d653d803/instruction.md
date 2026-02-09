# Bug Report

### Describe the bug

When creating a new client certificate with a valid `parentId`, the operation fails with an error stating that `parentId` is missing. The validation logic appears to be inverted - it throws an error when `parentId` is present instead of when it's missing.

### Reproduction

```js
// This should succeed but throws an error
const cert = create({
  parentId: 'wrk_123456',
  host: 'example.com',
  // ... other certificate properties
});

// Error: New ClientCertificate missing `parentId`: wrk_123456
```

### Expected behavior

Creating a client certificate with a `parentId` should succeed. The error should only be thrown when `parentId` is actually missing or undefined.

```js
// This SHOULD work
const cert = create({
  parentId: 'wrk_123456',
  host: 'example.com'
});

// This SHOULD throw the error
const cert = create({
  host: 'example.com'
  // missing parentId
});
```

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
