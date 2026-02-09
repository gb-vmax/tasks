# Bug Report

### Describe the bug

OAuth1 authentication with HMAC-SHA256 signature method is failing. When I configure a request to use OAuth1 with `HMAC-SHA256` as the signature method, the authentication fails with an invalid signature error from the API server.

### Reproduction

1. Set up a request with OAuth1 authentication
2. Configure signature method to `HMAC-SHA256`
3. Provide valid consumer key, consumer secret, token, and token secret
4. Send the request
5. Server responds with authentication failure (invalid signature)

The same credentials work fine when using external OAuth tools or when switching to `HMAC-SHA1` signature method in Insomnia.

### Expected behavior

The request should authenticate successfully when using `HMAC-SHA256` signature method. The OAuth signature should be generated using SHA256 hashing as specified by the signature method configuration.

### Additional context

This seems to have started happening recently. I've verified my credentials are correct by testing with other OAuth clients, and they work fine with HMAC-SHA256. The issue only occurs in Insomnia when specifically using the HMAC-SHA256 option.

---
Repository: /testbed
