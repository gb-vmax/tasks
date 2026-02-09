# Bug Report

### Describe the bug
When setting git author information, the name and email values appear to be swapped. After calling `setAuthor()`, the git config shows the email in the `user.name` field and the name in the `user.email` field.

### Reproduction
```js
const gitVCS = new GitVCS();

// Set author with name and email
await gitVCS.setAuthor('John Doe', 'john@example.com');

// Check the git config
const author = await gitVCS.getAuthor();

// Expected: author.name = 'John Doe', author.email = 'john@example.com'
// Actual: author.name = 'john@example.com', author.email = 'John Doe'
```

### Expected behavior
The `setAuthor()` method should correctly assign the name parameter to `user.name` and the email parameter to `user.email` in the git configuration. Currently, these values are reversed.

### System Info
- Insomnia version: latest
- OS: All platforms

---
Repository: /testbed
