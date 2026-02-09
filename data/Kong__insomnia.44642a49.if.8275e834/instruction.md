# Bug Report

### Describe the bug

The Git sync functionality is broken after a recent update. When trying to connect to a Git repository, the OAuth provider detection is not working correctly and authentication fails.

### Reproduction

```js
// Set up Git credentials with oauth2format
const credentials = {
  oauth2format: 'github',
  token: 'ghp_sometoken123'
}

// Try to get the OAuth provider name
const provider = getOauth2FormatName(credentials)
// Returns undefined instead of 'github'
```

### Expected behavior

The function should return the OAuth provider name ('github' or 'gitlab') when valid credentials are provided. Currently it's returning `undefined` even when the `oauth2format` field is explicitly set.

### Additional context

This is preventing me from syncing my workspace with GitHub. The authentication keeps failing because the provider format isn't being recognized properly.

---
Repository: /testbed
