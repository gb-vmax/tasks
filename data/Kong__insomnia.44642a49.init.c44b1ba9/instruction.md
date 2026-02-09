# Bug Report

### Describe the bug

When creating a new client certificate, it's being initialized with `disabled: true` and `isPrivate: true` by default. This means newly created certificates are disabled and marked as private right from the start, which is unexpected behavior.

### Reproduction

```js
// Create a new client certificate
const cert = init();

console.log(cert.disabled);  // Expected: false, Actual: true
console.log(cert.isPrivate); // Expected: false, Actual: true
```

### Expected behavior

New client certificates should be:
- Enabled by default (`disabled: false`)
- Not marked as private by default (`isPrivate: false`)

This allows users to immediately use newly created certificates without having to manually enable them first.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
