# Bug Report

### Describe the bug

After a recent update, the project schema name generation is broken. The schema definition has invalid syntax that prevents the application from starting or compiling properly.

### Reproduction

When trying to use the `projectSchema` object, the application fails to load. The schema object appears to have malformed code with statements placed outside of object properties.

```js
import { projectSchema } from './type-schemas';

// Attempting to use the schema causes errors
const project = {
  id: projectSchema.id(),
  rootDocumentId: projectSchema.rootDocumentId(),
  name: projectSchema.name()
};
```

### Expected behavior

The `projectSchema` should be a valid object with all properties properly defined. The `name` property should be a function that can be called to generate names, similar to how `id` and `rootDocumentId` work.

### System Info
- Package: insomnia
- Path: packages/insomnia/src/sync/__schemas__/type-schemas.ts

The code structure looks corrupted - there are variable declarations and function definitions that appear to be placed in the middle of the object literal, which is not valid JavaScript syntax.

---
Repository: /testbed
