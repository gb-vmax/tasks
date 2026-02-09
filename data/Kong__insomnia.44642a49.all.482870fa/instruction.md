# Bug Report

### Describe the bug

When fetching all git repositories, the application is crashing or behaving unexpectedly. It seems like the repository list sometimes contains null or undefined entries that aren't being handled properly.

### Reproduction

```js
// Fetch all git repositories
const repos = await gitRepository.all();

// Try to access repository properties
repos.forEach(repo => {
  console.log(repo.id); // Sometimes throws "Cannot read property 'id' of null"
});
```

### Expected behavior

The `all()` method should return only valid repository objects with defined `id` properties. Any null or undefined entries should be filtered out before being returned to prevent errors when accessing repository properties.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

---
Repository: /testbed
