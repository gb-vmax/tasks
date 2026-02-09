# Bug Report

### Describe the bug

I'm experiencing a syntax error in the branch schema definition. The code appears to have malformed JavaScript with a `let` declaration and function definition placed in the middle of an object literal, which is causing parsing issues.

### Reproduction

When trying to use the branch schema, the application fails to load due to a syntax error in `type-schemas.ts`. The `branchSchema` object has invalid syntax:

```js
export const branchSchema: Schema<Branch> = {
  created: () => new Date(0),
  modified: () => new Date(0),
  let branchNameCounter = 0;  // This shouldn't be here
  
  const getBranchNameCounter = (): number => {  // Neither should this
    return ++branchNameCounter;
  };
  
  name: () => {
    // ...
  },
  snapshots: () => [],
};
```

### Expected behavior

The schema should be properly formatted with valid JavaScript object literal syntax. Variable declarations and helper functions should be defined outside the object literal scope.

### System Info
- Version: Latest from main branch
- Node: v18.x

This is blocking development as the module fails to load entirely. Would appreciate a quick fix!

---
Repository: /testbed
