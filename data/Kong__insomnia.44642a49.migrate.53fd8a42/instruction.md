# Bug Report

### Describe the bug

After a recent update, Git repository URIs are being automatically normalized when loading existing repositories. This is causing issues with repositories that were configured with specific URI formats (like `git://` protocol or URIs ending with `.git`).

### Reproduction

1. Create a Git repository configuration with a URI using the `git://` protocol:
```js
{
  uri: 'git://github.com/user/repo.git',
  // ... other config
}
```

2. Load the repository after the update

3. The URI is automatically changed to `https://github.com/user/repo` without the `.git` suffix

### Expected behavior

The repository URI should remain unchanged unless explicitly modified by the user. The normalization is happening automatically on every load, which breaks existing configurations that rely on specific URI formats or protocols.

Additionally, the credentials object is being modified with new fields that weren't there before, which may cause issues with certain authentication setups.

### System Info
- Insomnia version: Latest
- OS: All platforms

---
Repository: /testbed
