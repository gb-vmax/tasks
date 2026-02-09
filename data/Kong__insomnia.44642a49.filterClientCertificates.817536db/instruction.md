# Bug Report

### Describe the bug

Client certificate matching is not working correctly when the host includes a port number. When I configure a certificate for a specific host with a port (e.g., `api.example.com:8443`), the certificate is not being selected for requests to that URL.

### Reproduction

1. Configure a client certificate with host `api.example.com:8443`
2. Make a request to `https://api.example.com:8443/endpoint`
3. The certificate is not applied to the request

It seems like the fallback logic that ignores port checking is not being triggered properly. The certificate should be matched even when the port doesn't match exactly, but currently it's only working when there's an exact match including the port.

### Expected behavior

The client certificate should be selected and applied to requests when:
- The host matches exactly (with port)
- OR the host matches without considering the port (fallback behavior)

Currently it appears the fallback matching (ignoring port) is not working as intended.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
