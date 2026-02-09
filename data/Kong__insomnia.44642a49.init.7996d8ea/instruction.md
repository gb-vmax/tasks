# Bug Report

### Describe the bug

When creating a new environment, it's being set as private by default instead of public. This is causing issues where environments that should be shared with the team are not visible to other users.

### Reproduction

```js
// Create a new environment
const env = init();

// Expected: isPrivate should be false
// Actual: isPrivate is true
console.log(env.isPrivate); // prints: true
```

### Steps to reproduce
1. Create a new environment using the init() function
2. Check the isPrivate property
3. The environment is private by default instead of public

### Expected behavior
New environments should be public (isPrivate: false) by default so they can be shared with team members. Users should explicitly opt-in to make environments private.

### Additional context
This seems to have changed recently and is affecting our workflow where we expect new environments to be visible to the whole team by default.

---
Repository: /testbed
