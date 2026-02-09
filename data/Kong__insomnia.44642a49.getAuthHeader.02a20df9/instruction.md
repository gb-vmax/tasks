# Bug Report

### Describe the bug

OAuth 2.0 and OAuth 1.0 authentication stopped working after a recent update. When making requests with OAuth authentication, no authorization header is being added to the request even though tokens are being fetched successfully.

### Reproduction

1. Set up a request with OAuth 2.0 authentication
2. Configure the OAuth 2.0 settings and obtain a valid access token
3. Send the request
4. The authorization header is missing from the outgoing request

Same issue occurs with OAuth 1.0:
1. Configure a request with OAuth 1.0 authentication
2. Set up all required OAuth 1.0 credentials
3. Send the request
4. No authorization header is included

### Expected behavior

When OAuth tokens are successfully retrieved, they should be included in the Authorization header of the outgoing request. The request should include:
- For OAuth 2.0: `Authorization: Bearer <access_token>` (or with custom prefix if configured)
- For OAuth 1.0: `Authorization: <oauth_signature_and_parameters>`

### Additional context

This seems to have broken recently. Previously OAuth authentication was working fine and tokens were being properly attached to requests. Now requests are going out without any authorization headers despite tokens being generated successfully.

---
Repository: /testbed
