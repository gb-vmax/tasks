# Bug Report

### Describe the bug

The GitLab OAuth token refresh is failing with a "No refresh token" error after the token has already been refreshed. It appears that when multiple requests try to refresh the token simultaneously, they're not properly coordinating and the refresh token gets cleared before subsequent requests can use it.

### Reproduction

```js
// Simulate multiple concurrent API calls that need token refresh
const promises = [
  makeGitLabApiCall(),
  makeGitLabApiCall(),
  makeGitLabApiCall()
];

await Promise.all(promises);
// Error: No refresh token
```

The issue happens when:
1. Multiple API calls are made at roughly the same time
2. All detect that the access token needs refreshing
3. They all try to call `refreshToken()` simultaneously
4. Some of them fail with "No refresh token" error

### Expected behavior

When multiple requests need to refresh the token at the same time, they should coordinate so that only one refresh happens and all requests wait for that single refresh to complete. The refresh token should remain available throughout the entire refresh process.

### System Info
- Insomnia version: latest
- OS: macOS

This is causing sync failures when working with GitLab repositories, especially when multiple operations are triggered in quick succession.

---
Repository: /testbed
