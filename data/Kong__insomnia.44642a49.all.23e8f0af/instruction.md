# Bug Report

### Describe the bug

After updating to the latest version, git repository operations are not reflecting changes correctly. When I create or remove a git repository, the changes don't appear in the UI until I restart the application. It seems like the repository list is being cached and not invalidating when modifications are made.

### Reproduction

1. Open Insomnia and connect to a git repository
2. Create a new git repository or remove an existing one using the UI
3. Navigate away and back to the git repositories view
4. The changes are not reflected - new repositories don't appear and removed ones are still showing

Alternatively, if you're using the API directly:

```js
// Create a new repository
await create({ uri: 'https://github.com/user/repo', credentials: {...} });

// Try to fetch all repositories
const repos = await all();
// The newly created repository doesn't appear in the list

// Or remove a repository
await remove(existingRepo);
const reposAfterRemoval = await all();
// The removed repository is still in the list
```

### Expected behavior

When git repositories are created or removed, subsequent calls to fetch all repositories should return the updated list immediately without requiring an application restart.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking our workflow as we need to restart the app every time we make changes to git repository configurations. Any help would be appreciated!

---
Repository: /testbed
