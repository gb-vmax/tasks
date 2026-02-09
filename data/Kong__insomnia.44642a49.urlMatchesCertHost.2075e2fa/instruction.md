# Bug Report

### Describe the bug

Client certificate hostname matching is not working correctly. When trying to use a client certificate with a specific hostname, the certificate is either being applied to the wrong hosts or not being applied at all.

### Reproduction

I have a client certificate configured for `api.example.com` but it seems to be matching incorrectly:

1. Set up a client certificate with host: `api.example.com`
2. Make a request to `api.example.com`
3. The certificate doesn't get applied

Also noticed that wildcard certificates seem to have issues:
- Certificate host: `*.example.com`
- Request to: `test.example.com`
- Expected: Certificate should be used
- Actual: Certificate is not being matched

Additionally, port matching appears to be inverted - certificates are only matching when ports DON'T match instead of when they DO match.

### Expected behavior

- Exact hostname matches should work correctly
- Wildcard patterns should match appropriately
- Port matching should only succeed when the ports actually match (not when they differ)

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
