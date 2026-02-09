# Bug Report

### Describe the bug

After a recent update, Git OAuth authentication is failing to connect. When I try to sync with my Git repository, the OAuth provider isn't being recognized properly and the authentication flow doesn't complete.

### Reproduction

```js
const credentials = {
  oauth2format: 'github',
  token: 'ghp_mytoken123'
};

// Try to get the OAuth provider name
const provider = getOauth2FormatName(credentials);
// Returns undefined instead of 'github'
```

### Steps to reproduce:
1. Set up Git sync with OAuth credentials
2. Specify the oauth2format as 'github' or 'gitlab'
3. Attempt to authenticate
4. The provider name is not recognized and authentication fails

### Expected behavior

The function should return the correct OAuth provider name ('github' or 'gitlab') when valid credentials are provided with the oauth2format field. The authentication should proceed normally.

### Additional context

This seems to have broken after some changes to the Git utils. The oauth2format field is being set correctly in the credentials object but it's not being returned by the getOauth2FormatName function. The function just returns undefined even when the credentials are valid.

---
Repository: /testbed
