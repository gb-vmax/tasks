# Bug Report

### Describe the bug
When setting Git author information, the name and email appear to be getting swapped. After calling `setAuthor()`, the user's name ends up stored as the email and vice versa.

### Reproduction
```js
const gitVcs = new GitVCS();

// Set author with name and email
await gitVcs.setAuthor('John Doe', 'john@example.com');

// Check the stored values
const author = await gitVcs.getAuthor();
console.log(author.name);  // Expected: 'John Doe', but shows 'john@example.com'
console.log(author.email); // Expected: 'john@example.com', but shows 'John Doe'
```

### Expected behavior
The `setAuthor()` method should correctly store the name parameter as `user.name` and the email parameter as `user.email` in the Git config. Currently they appear to be reversed.

### System Info
- Insomnia version: latest
- OS: Cross-platform issue

---
Repository: /testbed
