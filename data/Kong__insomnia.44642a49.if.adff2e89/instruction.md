# Bug Report

### Describe the bug

I'm encountering an issue with OAuth provider authentication in the Git sync functionality. When configuring Git credentials with OAuth2, the provider name doesn't seem to be recognized properly if it has different casing or extra whitespace.

### Reproduction

```js
const credentials = {
  oauth2format: 'GitHub'  // Capital 'H'
}

// Provider is not recognized even though it should be valid
const result = getOauth2FormatName(credentials)
// Returns undefined instead of 'github'
```

Similarly, if there's any whitespace:
```js
const credentials = {
  oauth2format: ' gitlab '
}

const result = getOauth2FormatName(credentials)
// Also returns undefined
```

### Expected behavior

The OAuth provider name should be case-insensitive and handle whitespace gracefully. Both 'GitHub', 'github', and ' github ' should be recognized as valid provider names and normalized to the correct format.

### System Info
- Version: latest
- OS: macOS

This is blocking our Git sync setup since users might enter provider names with different casing conventions. Would appreciate a fix for this!

---
Repository: /testbed
