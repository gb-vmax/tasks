# Bug Report

### Describe the bug

Client certificate matching is broken - certificates are not being properly selected for HTTPS requests. When making requests that should use a configured client certificate, the wrong certificate is selected or no certificate is used at all.

### Reproduction

1. Configure a client certificate for a specific host (e.g., `api.example.com`)
2. Make a request to that host
3. The certificate is not applied to the request

It seems like the certificate filtering logic is not correctly matching the request URL against the configured certificate hosts. Even with valid certificates configured, they're not being used for requests.

### Expected behavior

When a client certificate is configured for a host, it should be automatically selected and used when making requests to that host. The certificate matching should properly compare the request URL with the certificate's configured host pattern.

### Additional context

This appears to affect all client certificate configurations. The issue might be related to how disabled certificates are being handled in the fallback logic.

---
Repository: /testbed
