# Bug Report

### Describe the bug

I'm experiencing an issue with project creation where the `create()` function doesn't seem to be working properly. When I try to create a new project with custom properties, the properties aren't being saved correctly to the database.

### Reproduction

```js
import * as projectModel from './models/project';

// Try to create a project with a name
const project = projectModel.create({
  name: 'My New Project',
  parentId: 'wrk_123'
});

// The project is created but the properties are missing or incorrect
console.log(project.name); // undefined or not what was passed in
```

### Expected behavior

The `create()` function should accept a patch object and create a new project with those properties merged in. The returned project should have all the properties that were passed in the patch parameter.

### Additional context

This seems to have broken recently. Previously, creating projects with custom properties worked fine, but now it's not respecting the patch object that's passed to the `create()` function.

---
Repository: /testbed
