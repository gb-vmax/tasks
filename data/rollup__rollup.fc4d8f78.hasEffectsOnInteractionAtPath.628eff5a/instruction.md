# Bug Report

### Describe the bug

I'm experiencing an issue with property assignments not being properly tracked for side effects. When assigning values to properties returned from function calls, the bundler is incorrectly treating these assignments as pure operations and removing code that should be preserved.

### Reproduction

```js
// This assignment should be preserved but gets tree-shaken
getObject().property = value;

// The assignment has side effects but is being removed
functionReturningObject().field = 'test';
```

The bundler is treating these property assignments as if they have no side effects, causing the code to be eliminated during tree-shaking even though the assignments should be preserved.

### Expected behavior

Property assignments on objects returned from function calls should be recognized as having side effects and should not be removed during the build process. The generated bundle should include these assignment statements.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
