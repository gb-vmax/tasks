# Bug Report

### Describe the bug

I'm experiencing an issue with GitLab OAuth token refresh. After the recent update, I'm getting syntax errors when trying to sync with GitLab repositories. The application seems to have malformed code in the token refresh logic.

### Reproduction

1. Set up a GitLab repository sync
2. Wait for the OAuth token to expire (or manually trigger a token refresh)
3. Try to perform any Git operation (push, pull, etc.)
4. The application crashes with a syntax error

### Expected behavior

The token refresh should complete successfully and allow continued syncing with GitLab repositories without any errors.

### Additional context

This appears to be related to the GitLab OAuth provider implementation. The error prevents any GitLab sync operations from working at all. It looks like there might be some duplicate or malformed code in the refresh token function.

---
Repository: /testbed
