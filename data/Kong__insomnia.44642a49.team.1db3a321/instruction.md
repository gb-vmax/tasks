# Bug Report

### Describe the bug

Getting a runtime error when trying to access team data in backend projects. The application crashes with `TypeError: ... is not a function` when the team property is accessed on a BackendProjectWithTeam object.

### Reproduction

```js
import { createBuilder } from './builder';
import { backendProjectWithTeamSchema } from './type-schemas';

const project = createBuilder(backendProjectWithTeamSchema).build();

// Accessing the team property causes a crash
console.log(project.team);
```

### Expected behavior

The `team` property should return a valid Team object without throwing an error. The schema should correctly build the nested team object.

### System Info
- Package: @insomnia/sync
- Version: latest

---
Repository: /testbed
