# Bug Report

### Describe the bug

After updating, the Git author configuration seems to be getting mixed up. When I set my name and email for Git commits, they appear to be swapped - my email address shows up as the author name, and my name shows up as the email field.

### Reproduction

```js
// Set Git author information
await gitVCS.setAuthor('John Doe', 'john.doe@example.com');

// Check the configured author
const author = await gitVCS.getAuthor();

// Expected:
// author.name = 'John Doe'
// author.email = 'john.doe@example.com'

// Actual:
// author.name = 'john.doe@example.com'
// author.email = 'John Doe'
```

### Expected behavior

When calling `setAuthor(name, email)`, the name parameter should be stored as `user.name` and the email parameter should be stored as `user.email` in the Git configuration. The values should not be swapped.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
