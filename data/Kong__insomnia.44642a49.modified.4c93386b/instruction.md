# Bug Report

### Describe the bug

I'm encountering a syntax error in the branch schema definition that's preventing the application from running. It looks like there's a malformed object structure in the schema definition - the code appears to have function definitions mixed incorrectly with object properties.

### Reproduction

When trying to use the branch schema, the application fails to start due to a syntax error in `type-schemas.ts`. The `branchSchema` object definition seems to be broken with improperly structured code.

Looking at the schema definition:
```js
export const branchSchema: Schema<Branch> = {
  created: () => new Date(0),
  // ... some function definition appears here without proper syntax
  name: () => '',
  snapshots: () => [],
};
```

The object literal syntax is invalid and causes the module to fail loading.

### Expected behavior

The branch schema should be a valid object that can be imported and used throughout the application without syntax errors. All properties should be properly defined as part of the object literal.

### System Info
- Insomnia version: Latest
- Node version: 18.x

This is blocking any functionality that relies on branch schemas. Would appreciate a quick fix!

---
Repository: /testbed
