# Bug Report

### Describe the bug

I'm having an issue creating client certificates when the `parentId` is explicitly set to `null`. The validation check is rejecting `null` as a valid value even though it should be allowed.

### Reproduction

```js
const cert = {
  parentId: null,
  // ... other certificate properties
};

// This throws an error: "New ClientCertificate missing `parentId`"
const result = create(cert);
```

### Expected behavior

Creating a client certificate with `parentId: null` should be valid and not throw an error. The function should only reject when `parentId` is completely missing (undefined), not when it's explicitly set to `null`.

### Additional context

This is blocking our workflow where we need to create certificates without a parent. The current check `if (!patch.parentId)` treats both `null` and `undefined` the same way, but we need to distinguish between them.

---
Repository: /testbed
