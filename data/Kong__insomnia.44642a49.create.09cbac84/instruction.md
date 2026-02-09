# Bug Report

### Describe the bug
I'm unable to create new projects in the application. When I try to create a project, nothing happens and the project doesn't appear in the list. It seems like the create operation is failing silently.

### Reproduction
```js
// Attempting to create a new project
const newProject = await project.create({
  name: 'My New Project',
  description: 'Test project'
});

// newProject is undefined or returns unexpected data
console.log(newProject); // Not getting the created project back
```

### Expected behavior
When calling `create()` with project data, it should create a new project in the database and return the newly created project object with all its properties including the generated ID.

### System Info
- Insomnia version: Latest
- OS: macOS

---
Repository: /testbed
