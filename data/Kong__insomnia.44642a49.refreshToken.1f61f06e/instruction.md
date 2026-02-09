# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with GitLab OAuth token refresh functionality. The application appears to be making redundant token refresh requests even when a valid token already exists, and in some cases the refresh process seems to hang or fail unexpectedly.

### Reproduction

When working with GitLab integration:
1. Authenticate with GitLab OAuth
2. Perform actions that trigger token refresh
3. Notice that multiple refresh requests are being made in quick succession
4. Sometimes the refresh process appears to fail silently or takes much longer than expected

The behavior is inconsistent - sometimes it works fine, other times it seems to get stuck or make unnecessary requests.

### Expected behavior

Token refresh should:
- Only occur when the token is actually expired or when explicitly forced
- Complete reliably without hanging
- Not make redundant requests when a valid token exists
- Handle failures gracefully with proper error messages

### Additional context

This seems to have started happening after recent changes to the GitLab OAuth provider. The token refresh mechanism appears to have become more complex but isn't working as smoothly as before.

---
Repository: /testbed
