# Bug Report

### Describe the bug

After a recent update, creating a Git repository with a URI that has trailing slashes or ends with `.git` causes issues with repository matching and duplicate detection. The system is treating `https://github.com/user/repo` and `https://github.com/user/repo.git` as different repositories, even though they point to the same location.

### Reproduction

```js
// These should be treated as the same repository but aren't
const repo1 = create({ uri: 'https://github.com/user/repo' });
const repo2 = create({ uri: 'https://github.com/user/repo.git' });
const repo3 = create({ uri: 'https://github.com/user/repo/' });

// All three URIs point to the same repo but are stored differently
// Expected: All should normalize to the same URI format
// Actual: Each is stored with its original format
```

### Expected behavior

Git URIs should be normalized when creating a repository so that:
- Trailing slashes are removed
- The `.git` extension is handled consistently
- The same repository isn't created multiple times with slightly different URIs

This is causing problems with repository synchronization and duplicate prevention logic.

### Additional context

This appears to have started happening recently. Previously, URIs were being stored exactly as provided without any normalization, but now there seems to be some processing that's not working correctly.

---
Repository: /testbed
