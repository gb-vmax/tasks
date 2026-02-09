# Bug Report

### Describe the bug

After a recent update, I'm seeing issues with Git repository URIs being modified unexpectedly. When I set up a Git repository with a URI, it seems to be getting normalized/transformed automatically, which is breaking my workflow.

### Reproduction

```js
// Set up a Git repository with an HTTP URI
const repo = {
  type: 'GitRepository',
  uri: 'http://github.com/user/repo.git',
  credentials: {
    token: 'my-token'
  },
  author: {
    name: '  John Doe  ',
    email: '  john@example.com  '
  }
}

// After creating/loading the repository, the URI has been changed
// Expected: http://github.com/user/repo.git
// Actual: https://github.com/user/repo (protocol changed, .git removed)
```

### Expected behavior

The Git repository URI should remain exactly as I specified it. If I set it to use HTTP, it should stay HTTP. If I include the `.git` extension, it should be preserved.

Additionally, I'm noticing that credentials and author information are being trimmed/modified without my explicit request. While trimming whitespace might seem helpful, it's causing issues when the values are intentionally formatted a certain way.

### Additional context

This seems to have started happening recently. Previously, the repository configuration was stored exactly as provided. Now it appears that some automatic normalization is being applied, which is causing problems with:
- URIs that need to use HTTP instead of HTTPS
- Repository paths that include the `.git` suffix
- Credentials and author fields being automatically modified

Is there a way to disable this automatic normalization, or is this intended behavior? If it's intended, it would be helpful to have it documented so users know what transformations to expect.

---
Repository: /testbed
