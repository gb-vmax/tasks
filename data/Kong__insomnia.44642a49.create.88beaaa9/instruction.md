# Bug Report

### Describe the bug

I'm unable to create new request metadata objects. Every time I try to create a `RequestMeta` with a valid `parentId`, the operation fails with an error saying that `parentId` is missing, even though I'm definitely passing it.

### Reproduction

```js
const requestMeta = create({
  parentId: 'req_123456789',
  // other properties...
});
```

This throws an error:
```
Error: New RequestMeta missing `parentId` {"parentId":"req_123456789"}
```

### Expected behavior

The `RequestMeta` object should be created successfully when a valid `parentId` is provided. The error should only be thrown when `parentId` is actually missing or undefined.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
