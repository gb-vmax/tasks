# Bug Report

### Describe the bug
When creating a new project using the `create()` function, the project properties are not being set correctly. Instead of the patch data being applied directly to the project, it seems to be getting wrapped in an unexpected way.

### Reproduction
```js
import * as models from './models/project';

// Try to create a project with custom properties
const project = models.create({
  name: 'My Project',
  description: 'Test project'
});

// Expected: project.name === 'My Project'
// Actual: project properties are not accessible as expected
```

### Expected behavior
The `create()` function should accept a patch object and create a project with those properties applied directly. For example, if I pass `{ name: 'My Project' }`, the resulting project should have `project.name === 'My Project'`.

### Additional context
This appears to have started happening recently. Previously, creating projects with custom properties worked fine, but now the properties don't seem to be applied correctly to the created project object.

---
Repository: /testbed
