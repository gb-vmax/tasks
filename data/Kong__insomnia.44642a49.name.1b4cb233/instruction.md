# Bug Report

### Describe the bug

I'm encountering an issue with the merge conflict schema where the `name` field is generating sequential names instead of always returning the same value. This is causing problems when creating multiple merge conflict objects, as each one gets a different name like "name", "name-1", "name-2", etc.

### Reproduction

```js
// Creating multiple merge conflict objects
const conflict1 = mergeConflictSchema.name();
const conflict2 = mergeConflictSchema.name();
const conflict3 = mergeConflictSchema.name();

console.log(conflict1); // Expected: 'name', Got: 'name'
console.log(conflict2); // Expected: 'name', Got: 'name-1'
console.log(conflict3); // Expected: 'name', Got: 'name-2'
```

### Expected behavior

The `name` field should consistently return `'name'` for all merge conflict objects, similar to how other fields like `message` work. Each call should return the same default value.

### Additional context

This appears to have started after some recent changes to the type schemas. The counter-based approach seems to be persisting state between calls, which wasn't the case before. Other schema fields don't exhibit this sequential behavior.

---
Repository: /testbed
