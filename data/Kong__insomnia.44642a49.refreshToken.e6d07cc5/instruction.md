# Bug Report

### Describe the bug

The GitLab OAuth token refresh is broken after a recent change. When trying to refresh an expired token, I'm getting a syntax error and the refresh process completely fails.

### Reproduction

Steps to reproduce:
1. Set up GitLab OAuth integration
2. Wait for the access token to expire (or manually trigger a token refresh)
3. Try to perform any Git operation that requires authentication
4. The token refresh fails with a syntax error

The error occurs because there's invalid JavaScript syntax in the `refreshToken()` function - it looks like there's code after a return statement that shouldn't be there, causing a parsing error.

### Expected behavior

The token refresh should complete successfully and return a new access token. The function should handle retries with exponential backoff and properly store the new token with its expiration time.

### System Info
- Insomnia version: latest
- OS: Multiple (affects all platforms)

This is blocking any GitLab sync operations for users with expired tokens. The syntax error prevents the entire module from loading correctly.

---
Repository: /testbed
