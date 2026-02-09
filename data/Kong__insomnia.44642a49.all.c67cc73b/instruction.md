# Bug Report

### Describe the bug

The `all()` function in the git-repository model is returning a single repository object instead of an array of all repositories. This breaks any code that expects to iterate over multiple git repositories.

### Reproduction

```js
import * as gitRepository from './models/git-repository';

// Create multiple git repositories
const repo1 = await gitRepository.create({ /* ... */ });
const repo2 = await gitRepository.create({ /* ... */ });

// Try to get all repositories
const allRepos = await gitRepository.all();

// Expected: array with repo1 and repo2
// Actual: single repository object (not an array)
console.log(Array.isArray(allRepos)); // false
```

### Expected behavior

The `all()` function should return an array containing all git repositories in the database, allowing iteration and filtering operations.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
