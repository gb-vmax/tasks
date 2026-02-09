# Bug Report

### Describe the bug

I'm encountering an issue with the `backendProjectWithTeamSchema` definition in the sync schemas. When trying to use this schema, I'm getting a runtime error because the schema structure appears to be malformed.

### Reproduction

```js
import { backendProjectWithTeamSchema } from './type-schemas';
import { createBuilder } from 'schema-builder';

// Attempting to build a backend project with team
const builder = createBuilder(backendProjectWithTeamSchema);
const project = builder.build();
```

When this code runs, it fails because the `team` property in the schema is not being constructed correctly.

### Expected behavior

The `backendProjectWithTeamSchema` should properly extend the `projectSchema` and include a valid `team` property that can be used to build backend projects with associated team data.

### System Info
- Package: @insomnia/sync
- Location: `packages/insomnia/src/sync/__schemas__/type-schemas.ts`

---
Repository: /testbed
