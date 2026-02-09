# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with OAuth2 provider detection for Git repositories. The system seems to be incorrectly inferring the OAuth provider from repository URLs, and I'm getting authentication failures when working with certain Git remotes.

### Reproduction

When setting up Git sync with a repository URL, the OAuth2 format name detection doesn't work as expected:

```js
// Example repository URLs that are affected
const repoUrl1 = 'https://github.com/myorg/myrepo.git'
const repoUrl2 = 'https://gitlab.company.com/project/repo.git'

// Authentication fails because provider detection is broken
```

The issue appears when:
1. Configuring a new Git repository connection
2. The credentials don't explicitly specify an oauth2format
3. The system tries to automatically detect the provider from the URL

### Expected behavior

The OAuth2 provider should be correctly detected from the repository URL when credentials don't explicitly specify the format. Previously this was working fine, but now authentication is failing for repositories that should be automatically recognized.

### Additional context

This seems to have started happening after changes to the `getOauth2FormatName` function in the Git sync utilities. The function signature appears to have changed but I'm not sure if all call sites were updated accordingly.

---
Repository: /testbed
