# Bug Report

### Describe the bug

When creating a new project using the `create()` function with a patch object containing properties, none of the properties from the patch are being applied to the created project. The function seems to ignore all the data passed in and creates an empty project instead.

### Reproduction

```js
import * as projectModel from './models/project';

// Try to create a project with custom properties
const project = projectModel.create({
  name: 'My Project',
  parentId: 'wrk_123',
  description: 'Test project'
});

// Expected: project should have name, parentId, and description
// Actual: project is created but all properties are missing/default
console.log(project.name); // undefined or default value
console.log(project.parentId); // undefined or default value
```

### Expected behavior

The `create()` function should accept a patch object and apply all its properties to the newly created project. Any properties specified in the patch parameter should be present in the returned project object.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
