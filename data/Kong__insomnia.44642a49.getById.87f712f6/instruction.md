# Bug Report

### Describe the bug

After a recent update, I'm experiencing an issue where project updates aren't being reflected properly. When I update a project's properties (like name or settings), the old cached version is still being returned instead of the updated one.

### Reproduction

```js
// Get a project
const project = getById('project-123');
console.log(project.name); // 'Original Name'

// Update the project
update(project, { name: 'Updated Name' });

// Get the project again
const updatedProject = getById('project-123');
console.log(updatedProject.name); // Still shows 'Original Name' instead of 'Updated Name'
```

### Expected behavior

After updating a project, subsequent calls to `getById()` should return the project with the updated properties, not the cached version from before the update.

### Additional context

This seems to be related to some caching mechanism. The issue also occurs when removing projects - deleted projects can still be retrieved through `getById()` even after calling `remove()`.

---
Repository: /testbed
