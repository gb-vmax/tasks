# Bug Report

### Describe the bug

When using OAuth 1.0 authentication with the option to send credentials in query parameters, the OAuth parameters are not being added to the request URL. The authentication header is generated correctly, but when the authentication is configured to use query parameters instead of headers, the request is sent without the necessary OAuth parameters in the query string.

### Reproduction

1. Create a request with OAuth 1.0 authentication
2. Configure OAuth 1.0 to send credentials as query parameters (not in the Authorization header)
3. Send the request
4. Observe that the OAuth parameters (oauth_consumer_key, oauth_signature, etc.) are missing from the URL query string

Expected OAuth parameters like `oauth_consumer_key`, `oauth_nonce`, `oauth_signature`, `oauth_signature_method`, `oauth_timestamp`, `oauth_token`, and `oauth_version` should be appended to the request URL as query parameters.

### Expected behavior

The OAuth 1.0 parameters should be properly extracted and added as query parameters when the authentication is configured to use query string instead of headers. The request URL should include all necessary OAuth parameters for authentication.

### System Info
- Insomnia version: latest
- OS: All platforms

---
Repository: /testbed
