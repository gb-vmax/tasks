# Bug Report

### Describe the bug

After a recent update, the project schema's `id` field is generating inconsistent IDs. When creating multiple projects in sequence, they all end up with the same `id` value instead of unique identifiers.

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

// All projects have the same ID!
console.log(project1.id === project2.id); // true (should be false)
```

### Expected behavior

Each call to `projectSchema.id()` should return a unique identifier so that multiple projects can be distinguished from each other. Currently all projects end up with the same ID which causes conflicts when trying to manage multiple projects.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
