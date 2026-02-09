# Bug Report

### Describe the bug

I'm having trouble creating client certificates in Insomnia. After a recent update, I'm getting validation errors when trying to add certificates that previously worked fine.

### Reproduction

When I try to create a disabled client certificate without specifying the host, I get an error even though the certificate is disabled:

```js
create({
  parentId: 'wrk_123',
  disabled: true,
  cert: 'cert-content',
  key: 'key-content'
})
```

This throws an error about missing `host`, but since the certificate is disabled, I shouldn't need to provide a host yet.

Also, if I try to create a disabled certificate with just a pfx file:

```js
create({
  parentId: 'wrk_123',
  disabled: true,
  pfx: 'pfx-content'
})
```

I'm getting validation errors about missing cert/key pairs even though I'm using pfx format and the certificate is disabled.

### Expected behavior

Disabled certificates should be allowed to be created without full validation since they won't be used until they're enabled. I should be able to:
- Create a disabled certificate without a host
- Create a disabled certificate with incomplete certificate data (e.g., only pfx, or only cert without key)

This would allow me to save work-in-progress certificates and enable them later once I have all the required information.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
