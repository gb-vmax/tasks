# Bug Report

### Describe the bug
GitLab OAuth token refresh is broken after a recent change. When attempting to refresh an expired access token, the application fails to properly authenticate with GitLab and users are unable to sync their projects.

### Reproduction
1. Set up GitLab sync with OAuth authentication
2. Wait for the access token to expire (or manually invalidate it)
3. Try to perform any Git operation that requires authentication
4. The token refresh fails and users are logged out

### Expected behavior
The refresh token flow should successfully exchange the refresh token for a new access token and continue the Git operation seamlessly without requiring the user to re-authenticate.

### Additional context
This appears to have started happening recently. The token refresh endpoint is being called but something in the request format seems incorrect. Users are being forced to re-authenticate manually every time their tokens expire which is very disruptive to the workflow.

---
Repository: /testbed
