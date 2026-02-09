# Bug Report

### Describe the bug

After a recent update, the `backendProjectWithTeamSchema` appears to have a syntax error that prevents the application from running. When trying to use any functionality that relies on this schema, the app crashes immediately.

### Reproduction

```js
import { backendProjectWithTeamSchema } from './type-schemas';

// Attempting to use the schema causes a crash
const project = createBuilder(backendProjectWithTeamSchema).build();
```

### Expected behavior

The schema should be properly defined and the application should run without syntax errors. The `team` property should be correctly integrated into the schema object.

### Additional context

This seems to have been introduced in a recent commit that modified the `backendProjectWithTeamSchema` definition. The code structure looks malformed - there appear to be variable declarations and helper functions placed in an incorrect location within the schema object definition.

The original schema had a simple `team` property, but now there's code that looks like it was meant to be outside the object literal but ended up inside it instead.

---
Repository: /testbed
