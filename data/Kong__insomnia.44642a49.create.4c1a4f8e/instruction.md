# Bug Report

### Describe the bug

After a recent update, I'm unable to create Git repositories with relative paths or custom URI schemes. The application now throws an error when trying to set up a repository with a path that doesn't start with one of the standard protocols.

### Reproduction

```js
// This used to work but now throws an error
const repo = create({
  uri: '/path/to/local/repo'
});

// Also fails with custom schemes
const customRepo = create({
  uri: 'custom://my-repo'
});
```

The error message says: `Invalid Git repository URI: must start with a valid protocol`

### Expected behavior

The application should accept relative paths and local file paths for Git repositories, not just URLs with specific protocols. Many users work with local repositories that don't use the standard git:// or https:// protocols.

### Additional context

This appears to have started happening recently. Previously, I could create repositories with local paths without any issues. The validation seems too strict and is blocking legitimate use cases for local development.

---
Repository: /testbed
