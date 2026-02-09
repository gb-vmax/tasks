# Bug Report

### Describe the bug

When setting `request.certificate` to `null` in a pre-request script, the client certificates are not being cleared as expected. The original certificates are still being used instead of being removed.

### Reproduction

```js
// In pre-request script
pm.request.certificate = null;
```

After setting the certificate to `null`, the request still uses the original client certificates that were configured. It seems like `null` values are not being handled correctly and the function falls back to returning the original certificates.

### Expected behavior

Setting `request.certificate` to `null` should clear/remove all client certificates for that request. The request should proceed without any client certificates attached.

### Additional context

This appears to be related to how the certificate merging logic handles falsy values. The condition checking for `!updatedReq.certificate` should treat `null` as a signal to clear certificates, but currently it just returns the original certificates unchanged.

---
Repository: /testbed
