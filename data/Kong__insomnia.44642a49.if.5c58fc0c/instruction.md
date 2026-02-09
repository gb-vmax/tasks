# Bug Report

### Describe the bug
I'm experiencing an issue with client certificate handling after a recent update. It seems like the certificate merging logic has been changed, and now when I try to set client certificates through the pre-request script, the behavior is inconsistent.

### Reproduction
```js
// In pre-request script
const cert = {
  key: 'path/to/key.pem',
  cert: 'path/to/cert.pem',
  passphrase: 'my-passphrase'
};

insomnia.request.certificate = cert;
```

When running the request, the certificate doesn't seem to be applied correctly. The original workspace certificates are being used instead of the one I'm setting in the script.

### Expected behavior
When setting a certificate in the pre-request script, it should override or merge with the existing client certificates properly. The request should use the certificate I specified.

### Additional context
This was working fine before. I'm not sure if this is related to how certificates with wildcard hosts are being matched or if there's something else going on with the merging logic.

---
Repository: /testbed
