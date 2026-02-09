# Bug Report

### Describe the bug
When creating a new project using the `create()` function, all properties are being set to `undefined` instead of using the values passed in the `patch` parameter. This causes newly created projects to have no data.

### Reproduction
```js
import * as project from './models/project';

// Try to create a project with specific properties
const newProject = project.create({
  name: 'My Project',
  description: 'A test project'
});

console.log(newProject.name); // Expected: 'My Project', Actual: undefined
console.log(newProject.description); // Expected: 'A test project', Actual: undefined
```

### Expected behavior
The `create()` function should use the properties provided in the `patch` parameter to initialize the project. All fields passed in `patch` should be set to their provided values, not `undefined`.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
