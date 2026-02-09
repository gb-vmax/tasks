# Bug Report

### Describe the bug

I'm experiencing an issue where assignment operations to member expressions are not being handled correctly. When assigning to object properties, the code seems to be including the wrong paths or applying deoptimizations at the wrong time.

### Reproduction

```js
const obj = {
  foo: {
    bar: 1
  }
};

// Assignment to nested property
obj.foo.bar = 2;

// The assignment target is not being processed correctly
// and the path inclusion logic seems inverted
```

### Expected behavior

When assigning to a member expression, the assignment deoptimization should only be applied if it hasn't been applied yet (i.e., when `assignmentDeoptimized` is `false`). Additionally, the path should be included when the member is NOT undefined, not when it IS undefined.

The current behavior appears to have the logic inverted - it's checking for the opposite conditions of what should actually trigger the inclusion.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
