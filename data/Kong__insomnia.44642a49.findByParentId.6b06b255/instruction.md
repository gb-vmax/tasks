# Bug Report

### Describe the bug
I'm unable to retrieve client certificates using `findByParentId()`. The function seems to be returning an empty array regardless of what `parentId` I pass to it. This is breaking certificate management in my workspace.

### Reproduction
```js
// Try to find certificates by parent ID
const certs = findByParentId('wrk_abc123');

// Returns empty array even though certificates exist
console.log(certs); // []
```

### Expected behavior
The function should return all client certificates that match the given `parentId`. Currently it's not returning any certificates at all, even when they exist in the database.

### Additional context
This seems to have started recently - certificate lookup was working fine before. Now I can't access any of my configured client certificates through the API, which is blocking my workflow.

---
Repository: /testbed
