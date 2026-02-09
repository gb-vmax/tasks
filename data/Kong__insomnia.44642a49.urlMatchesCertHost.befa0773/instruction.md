# Bug Report

### Certificate host matching not working correctly

I'm experiencing an issue where SSL certificate host validation is failing for valid HTTPS requests. It seems like certificates are not being properly matched to their corresponding hosts.

### Reproduction

When making HTTPS requests with client certificates configured:

1. Set up a client certificate for a specific host (e.g., `api.example.com`)
2. Make an HTTPS request to that host
3. The certificate is not applied to the request even though the host matches

The certificate should be matched and applied to requests going to the configured host, but it's not being recognized as a match.

### Expected behavior

When a certificate is configured for a specific host, requests to that host (or matching wildcard patterns) should use the certificate. The host matching logic should correctly validate that the request URL matches the certificate's configured host.

### Additional context

This appears to be affecting HTTPS requests specifically. The matching seems to work in reverse - rejecting valid matches instead of accepting them.

---
Repository: /testbed
