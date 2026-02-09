# Bug Report

### Describe the bug

When trying to retrieve all git repositories, the function returns a single repository object instead of an array of repositories. This breaks any code that expects to iterate over multiple repositories.

### Reproduction

```js
const repos = await gitRepository.all();

// Expected: repos should be an array that can be iterated
// Actual: repos is a single object, not an array

repos.forEach(repo => {
  console.log(repo.name); // TypeError: repos.forEach is not a function
});
```

### Expected behavior

The `all()` function should return an array of GitRepository objects, allowing iteration over all repositories in the database.

### Additional context

This appears to affect any workflow that needs to list or process multiple git repositories. The return type suggests it should be an array but the actual value returned is not iterable.

---
Repository: /testbed
