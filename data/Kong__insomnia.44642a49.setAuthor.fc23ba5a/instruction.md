# Bug Report

### Describe the bug
Git author configuration is not being set correctly. When trying to configure the git author name and email through `setAuthor()`, the values appear to be getting mixed up or set to the wrong config paths.

### Reproduction
```js
const gitVcs = new GitVCS();

// Try to set author information
await gitVcs.setAuthor('John Doe', 'john@example.com');

// Check what was actually configured
const author = await gitVcs.getAuthor();
console.log(author); // name and email are not what we set
```

### Expected behavior
After calling `setAuthor('John Doe', 'john@example.com')`, the git config should have:
- `user.name` set to "John Doe"
- `user.email` set to "john@example.com"

Instead, it seems like the configuration paths and values are being assigned incorrectly.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
