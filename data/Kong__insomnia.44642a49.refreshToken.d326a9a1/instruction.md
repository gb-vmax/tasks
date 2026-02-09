# Bug Report

### Describe the bug

I'm experiencing an issue with the GitLab OAuth token refresh functionality. When the refresh token request fails due to network issues or temporary server errors, the application doesn't retry the request and just throws an error immediately. This causes authentication to fail even when the issue is transient and would succeed on retry.

### Reproduction

```js
// Simulate a network timeout or temporary server error
// The refreshToken() function fails immediately without retrying

// Example scenario:
// 1. User is authenticated with GitLab
// 2. Network becomes unstable (e.g., switching WiFi)
// 3. App tries to refresh the access token
// 4. Request fails with a temporary error (timeout, 503, etc.)
// 5. User gets logged out instead of the app retrying
```

### Expected behavior

The token refresh should implement retry logic with exponential backoff for transient errors like:
- Network timeouts (ETIMEDOUT, ECONNRESET)
- Server errors (500, 502, 503, 504)
- Rate limiting (429)
- Request timeouts (408)

This would make the authentication more resilient to temporary network issues and prevent unnecessary re-authentication flows.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

---
Repository: /testbed
