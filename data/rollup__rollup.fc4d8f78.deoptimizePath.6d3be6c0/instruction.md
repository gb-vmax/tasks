# Bug Report

### Describe the bug

I'm encountering an issue where destructured function parameters are being incorrectly treated as reassigned when accessing nested properties. This causes the bundler to produce overly conservative output that doesn't properly tree-shake unused code.

### Reproduction

```js
function processUser({ profile }) {
  return profile.name;
}

const user = {
  profile: {
    name: 'John',
    age: 30
  }
};

processUser(user);
```

When bundling code like this, the parameter `profile` is being marked as reassigned even though we're only accessing a nested property (`profile.name`). This prevents proper optimization and results in larger bundle sizes.

### Expected behavior

Accessing nested properties on destructured parameters should not mark the parameter itself as reassigned. Only actual reassignments or mutations should trigger this behavior. The bundler should be able to properly track property access without assuming the entire parameter is modified.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently, possibly after some changes to how parameter variables handle path deoptimization. The issue specifically occurs when accessing properties at depth > 1 on function parameters.

---
Repository: /testbed
