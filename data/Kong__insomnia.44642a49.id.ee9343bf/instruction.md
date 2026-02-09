# Bug Report

### Describe the bug

I'm experiencing a syntax error in the codebase after a recent update. The application fails to start and throws a parsing error related to the team schema definition.

### Reproduction

The error occurs when trying to import or use the team schema from `type-schemas.ts`. The application won't compile/start at all.

```js
import { teamSchema } from './sync/__schemas__/type-schemas';

// Application crashes on import
```

### Expected behavior

The team schema should be properly defined and the application should start without syntax errors. The schema object should have valid JavaScript syntax with proper property definitions.

### Additional context

This appears to have broken after some changes to how team IDs are generated. The code structure in the schema definition looks malformed - there seems to be a function declaration mixed into the object literal in an invalid way.

The schema should follow the same pattern as other schemas in the file (like `projectSchema`) where properties are defined correctly within the object.

---
Repository: /testbed
