# Bug Report

### Describe the bug

After a recent update, I'm unable to create new request groups in my workspace. The application throws an error about missing functions whenever I try to create a new folder or perform basic operations on request groups.

### Reproduction

```js
// Attempting to create a new request group
const newGroup = await RequestGroup.create({
  parentId: 'wrk_123',
  name: 'My New Folder'
});

// Error: RequestGroup.create is not a function
```

Also happens when trying to:
- Get a request group by ID
- Update an existing request group
- Remove a request group
- List all request groups

### Expected behavior

The basic CRUD operations for request groups should work as before. Functions like `create()`, `getById()`, `update()`, `remove()`, and `all()` should be available and functional.

### System Info
- Insomnia version: latest
- OS: macOS

It seems like the core request group model functions have been removed or relocated. This is blocking me from organizing my API requests into folders.

---
Repository: /testbed
