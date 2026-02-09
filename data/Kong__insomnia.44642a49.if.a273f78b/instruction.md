# Bug Report

### Environment loading returns undefined instead of null when no environments exist

I'm experiencing an issue with environment loading in inso where the behavior has changed unexpectedly. When there are no environments in the database, the `loadEnvironment` function now returns `undefined` instead of `null`.

### Reproduction
```js
const db = {
  Environment: []
};

const result = loadEnvironment(db, 'workspace-id');
// result is now undefined, but used to be null
```

### Expected behavior
The function should return `null` when the Environment array is empty, as it did before. This is causing issues in code that explicitly checks for `null` vs `undefined` to distinguish between "no environments exist" and other error conditions.

### Additional context
This seems to have changed recently. The check was modified from `!db.Environment.length` to `!db.Environment`, which changes the return value when the Environment array exists but is empty.

---
Repository: /testbed
