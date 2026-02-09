# Bug Report

### Describe the bug

After a recent update, I'm unable to create projects with certain `remoteId` formats. The project creation is failing with an error about invalid remoteId format, even though the remoteId I'm passing should be valid.

### Reproduction

```js
// This used to work but now throws an error
await project.create({
  name: 'My Project',
  remoteId: 'custom_project_id_123'
});

// Error: Invalid remoteId format
```

I have existing projects in my database that use custom remoteId formats (not starting with `proj_team`, `proj_org`, or the standard prefix), and now I can't create new projects with similar IDs.

### Expected behavior

The project should be created successfully with the custom remoteId, or at minimum, the validation should be more flexible to accommodate different remoteId formats that were previously allowed.

### Additional context

This appears to have broken backward compatibility with existing projects that use custom remoteId schemes. Also noticed that creating multiple scratchpad projects now throws an error, which might be intentional but wasn't documented.

---
Repository: /testbed
