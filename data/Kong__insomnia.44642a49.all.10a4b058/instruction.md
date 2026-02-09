# Bug Report

### Describe the bug

After a recent update, the `all()` function for git repositories is now returning repositories in a different order than before. Previously, repositories were returned in the order they were created/stored in the database, but now they appear to be sorted alphabetically by URI.

This is breaking our workflow where we rely on the insertion order to display the most recently added repositories at the top of the list.

### Reproduction

```js
// Add repositories in this order
await create({ uri: 'https://github.com/user/zebra-repo', ... });
await create({ uri: 'https://github.com/user/alpha-repo', ... });
await create({ uri: 'https://github.com/user/beta-repo', ... });

// Fetch all repositories
const repos = await all();

// Expected order: zebra-repo, alpha-repo, beta-repo (insertion order)
// Actual order: alpha-repo, beta-repo, zebra-repo (alphabetically sorted)
```

### Expected behavior

The `all()` function should return repositories in their original insertion order, not sorted alphabetically. If sorting is needed, it should be opt-in or handled at the UI layer, not in the data access layer.

### Additional context

This change appears to have been introduced recently and is affecting our repository list display. We have UI code that depends on the natural database ordering to show recently added repositories first.

---
Repository: /testbed
