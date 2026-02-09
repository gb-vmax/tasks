# Bug Report

### Describe the bug

Client certificate matching is not working correctly - certificates are failing to match when they should be applied to requests. It seems like the host/port validation logic is inverted, causing valid certificate configurations to be rejected and invalid ones to potentially be accepted.

### Reproduction

Set up a client certificate with the following configuration:
- Certificate host: `api.example.com`
- Port: `443`

Try to make a request to:
- URL: `https://api.example.com/endpoint`

Expected: The certificate should be matched and applied to the request
Actual: The certificate is not being matched/applied

The same issue occurs with wildcard hosts like `*.example.com` - they're not matching subdomains that they should match.

### Expected behavior

Client certificates should be correctly matched against request URLs based on hostname and port. When a certificate is configured for a specific host/port combination, it should be applied to requests matching that configuration.

### Additional context

This appears to affect all certificate matching logic, including:
- Exact hostname matches
- Wildcard hostname patterns
- Port-specific configurations

---
Repository: /testbed
