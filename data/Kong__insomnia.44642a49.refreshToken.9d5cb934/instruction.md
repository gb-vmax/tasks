# Bug Report

### Describe the bug
After refreshing GitLab OAuth tokens, I'm unable to authenticate with GitLab repositories. The authentication keeps failing even though the token refresh appears to succeed without errors.

### Reproduction
1. Set up GitLab integration with OAuth
2. Wait for the access token to expire
3. Trigger a token refresh (e.g., by trying to sync with a GitLab repository)
4. Subsequent API calls to GitLab fail with authentication errors

### Expected behavior
After the token refresh completes, I should be able to continue working with GitLab repositories without authentication issues. The new access token should be properly stored and used for subsequent requests.

### Additional context
This seems to have started happening recently. The token refresh operation itself doesn't throw any errors, but the stored tokens don't seem to work correctly afterwards. I have to manually re-authenticate through the OAuth flow to get things working again.

---
Repository: /testbed
