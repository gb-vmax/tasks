# Bug Report

### Describe the bug
When setting the Git author information using `setAuthor()`, the name and email values appear to be getting swapped. After calling `setAuthor(name, email)`, the name is stored in the email field and the email is stored in the name field.

### Reproduction
```js
// Set author with name and email
await gitVcs.setAuthor('John Doe', 'john@example.com');

// Get the author back
const author = await gitVcs.getAuthor();

// Expected: { name: 'John Doe', email: 'john@example.com' }
// Actual: { name: 'john@example.com', email: 'John Doe' }
```

### Expected behavior
The `setAuthor()` method should correctly store the name parameter as `user.name` and the email parameter as `user.email` in the Git config. Currently they seem to be reversed.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
