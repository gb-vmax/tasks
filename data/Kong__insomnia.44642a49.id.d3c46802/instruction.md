# Bug Report

### Describe the bug

After a recent update, the `projectSchema.id` field is not generating unique IDs as expected. When creating multiple project objects using the schema, they all end up with the same ID value instead of having unique identifiers.

### Reproduction

```js
import { projectSchema } from './type-schemas';

// Create multiple projects
const project1 = { id: projectSchema.id() };
const project2 = { id: projectSchema.id() };
const project3 = { id: projectSchema.id() };

console.log(project1.id); // Expected: unique ID, Actual: 'id'
console.log(project2.id); // Expected: unique ID, Actual: 'id'
console.log(project3.id); // Expected: unique ID, Actual: 'id'

// All three projects have the same ID
```

### Expected behavior

Each call to `projectSchema.id()` should generate a unique identifier, or at least support configuration options to enable counter-based ID generation. The current implementation just returns the static string 'id' for all invocations, which causes ID collisions when creating multiple project instances.

### System Info
- Package: @insomnia/sync
- Node version: 18.x

This is blocking our ability to work with multiple projects simultaneously since they all share the same identifier. Any workaround suggestions would be appreciated while this gets fixed.

---
Repository: /testbed
