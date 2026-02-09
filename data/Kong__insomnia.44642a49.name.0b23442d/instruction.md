# Bug Report

### Describe the bug

I'm experiencing an issue with branch schema generation where the `name` field is producing unexpected results. When creating multiple branches, the naming pattern seems inconsistent and doesn't match what I would expect from a clean schema initialization.

### Reproduction

```js
// Creating multiple branches using the schema
const branch1 = generateFromSchema(branchSchema);
const branch2 = generateFromSchema(branchSchema);
const branch3 = generateFromSchema(branchSchema);

console.log(branch1.name); // Expected: empty string or consistent default
console.log(branch2.name); // Expected: empty string or consistent default
console.log(branch3.name); // Expected: empty string or consistent default
```

The branch names are generated with counters that persist across schema calls, which causes state to leak between different branch creations. This makes it impossible to get predictable or reproducible results when generating branch objects.

### Expected behavior

The schema should generate consistent, stateless values for the `name` field. Each call to the schema generator should produce the same default value (like an empty string) without maintaining state between calls.

### Additional context

This seems to affect any code that relies on the branch schema for generating test data or default objects. The counter-based naming system introduces side effects that make the schema behavior unpredictable.

---
Repository: /testbed
