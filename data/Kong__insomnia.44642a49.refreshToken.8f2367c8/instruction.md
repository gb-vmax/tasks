# Bug Report

### Describe the bug

When trying to refresh GitLab OAuth tokens, the application hangs indefinitely and never completes the token refresh operation. This appears to be causing authentication failures when the access token expires.

### Reproduction

1. Set up GitLab OAuth integration with Insomnia
2. Wait for the access token to expire (or manually trigger a token refresh)
3. The token refresh process starts but never completes
4. Application becomes unresponsive during authentication attempts

### Expected behavior

The token refresh should complete successfully and return a new access token, allowing continued use of the GitLab integration without hanging.

### System Info
- Insomnia version: latest
- GitLab OAuth provider integration

---
Repository: /testbed
