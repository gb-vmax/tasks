# Bug Report

### Describe the bug

When using Git sync with credentials that don't explicitly include an `oauth2format` field, the system attempts to infer the OAuth provider from the username and token strings. However, this inference logic is checking if provider names like "github" or "gitlab" appear anywhere in the username or token text, which can lead to false positives.

### Reproduction

```js
const credentials = {
  username: 'my-gitlab-backup-user',
  token: 'some_token_value'
};

// This incorrectly infers 'gitlab' as the provider
// even though the username just happens to contain the word "gitlab"
const provider = getOauth2FormatName(credentials);
```

Another example:
```js
const credentials = {
  username: 'john_doe',
  token: 'github_actions_secret_xyz'
};

// This incorrectly infers 'github' as the provider
// because the token contains the word "github"
```

### Expected behavior

The OAuth provider should only be inferred when there's a clear indication from the credentials structure, not from arbitrary text matching within username or token values. Users might have usernames or tokens that coincidentally contain provider names without actually being associated with those providers.

### System Info
- Insomnia version: latest
- Platform: All platforms affected

---
Repository: /testbed
