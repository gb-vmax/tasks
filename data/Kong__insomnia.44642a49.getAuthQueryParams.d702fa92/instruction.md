# Bug Report

### Describe the bug

I'm experiencing an issue with OAuth 1.0 authentication when query parameters are being generated. It seems like the system isn't properly handling OAuth 1.0 parameters that need to be added to the query string.

### Reproduction

When making a request with OAuth 1.0 authentication configured to use query parameters (instead of headers), the OAuth signature and related parameters aren't being included in the URL query string.

Steps to reproduce:
1. Configure a request with OAuth 1.0 authentication
2. Set the authentication to pass credentials via query parameters
3. Send the request
4. Check the actual URL being sent - OAuth parameters are missing

### Expected behavior

The OAuth 1.0 parameters (oauth_consumer_key, oauth_token, oauth_signature, oauth_timestamp, oauth_nonce, etc.) should be properly extracted and added to the query string when OAuth 1.0 authentication is configured to use query parameters instead of headers.

Currently it seems like the query params generation doesn't account for OAuth 1.0 at all, only handling bearer tokens.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
