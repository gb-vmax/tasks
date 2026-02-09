# Bug Report

### Describe the bug
After a recent update, the GitLab OAuth flow is failing during authorization. When attempting to authenticate with GitLab, the authorization URL generation seems to be broken and the OAuth handshake doesn't complete successfully.

### Reproduction
```js
// Try to generate GitLab authorization URL
const authUrl = await generateAuthorizationUrl();

// The generated URL appears to have issues with the code challenge parameter
// Authentication fails when redirected to GitLab
```

### Steps to reproduce:
1. Configure GitLab sync integration
2. Attempt to authorize with GitLab OAuth
3. The authorization process fails or behaves unexpectedly

### Expected behavior
The GitLab OAuth authorization flow should complete successfully and generate a valid authorization URL with proper PKCE challenge parameters.

### Additional context
This seems related to how the code verifier challenge is being generated. The authorization URL might be malformed or the challenge parameter isn't being calculated correctly.

---
Repository: /testbed
