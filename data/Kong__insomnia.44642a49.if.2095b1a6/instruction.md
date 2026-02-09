# Bug Report

### Describe the bug
After a recent update, OAuth2 provider names are no longer being recognized correctly in Git sync. When I try to use provider names like "GitHub" or "GitLab" (with different capitalizations), the authentication fails silently.

### Reproduction
```js
const credentials = {
  oauth2format: 'GitHub'  // or 'GITHUB', 'GitLab', etc.
}

// Provider name is not recognized anymore
const provider = getOauth2FormatName(credentials)
// Returns undefined instead of 'github' or 'gitlab'
```

### Expected behavior
The function should handle different capitalizations of provider names (e.g., "GitHub", "GITHUB", "github") and return the normalized lowercase version ('github' or 'gitlab'). Previously this worked fine regardless of capitalization.

### Additional context
This is breaking my Git sync setup since I had the provider name stored with capital letters. It seems like the function is now case-sensitive when it wasn't before.

---
Repository: /testbed
