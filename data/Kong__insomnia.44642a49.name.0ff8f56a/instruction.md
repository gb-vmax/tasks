# Bug Report

### Describe the bug

When creating multiple projects through the sync schema, the project names are being generated with random suffixes and counter values instead of using a consistent "name" value. This causes issues when trying to reference or identify projects consistently across operations.

### Reproduction

```js
// Creating multiple projects
const project1 = createProject(); // Expected: 'name', Actual: 'name-0-a3f2'
const project2 = createProject(); // Expected: 'name', Actual: 'item-1-b7k9'
const project3 = createProject(); // Expected: 'name', Actual: 'entity-2-c1m4'

// Each project gets a different name pattern with counters and random strings
console.log(project1.name); // 'name-0-a3f2'
console.log(project2.name); // 'item-1-b7k9'
console.log(project3.name); // 'entity-2-c1m4'
```

### Expected behavior

All projects should have the same consistent name value ('name') when generated through the schema. The name field shouldn't include random suffixes or rotating patterns.

### Additional context

This appears to be affecting the `projectSchema` in the sync type schemas. The name generator is using a global counter and cycling through different patterns ('name', 'item', 'entity', 'object', 'resource') which makes it impossible to predict or rely on project names.

---
Repository: /testbed
