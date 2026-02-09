# Bug Report

### Describe the bug

After a recent update, the `projectSchema` is not generating IDs correctly. The schema appears to be defining complex ID generation logic including sequential ID generation and prefix detection, but the actual `id` field is not a simple function anymore - it's been replaced with what looks like implementation code that shouldn't be in the schema definition itself.

### Reproduction

```ts
import { projectSchema } from './type-schemas';

// Try to use the schema
const project = {
  id: projectSchema.id(),
  rootDocumentId: projectSchema.rootDocumentId(),
  name: projectSchema.name(),
};

console.log(project.id); // Expected: 'id', but getting syntax errors or undefined
```

### Expected behavior

The `projectSchema.id()` function should return a simple string value like `'id'`, consistent with the other schema fields (`rootDocumentId`, `name`). The schema definition should be clean and not contain implementation logic mixed with the schema structure.

### Additional context

It looks like there's a syntax error in the schema definition where the `id` field has interface definitions, function declarations, and variables declared inside the schema object itself. This breaks the schema structure and causes the ID generation to fail.

The other fields in the schema (`rootDocumentId`, `name`) work fine and return their expected values, but the `id` field is completely broken.

---
Repository: /testbed
