# Bug Report

### Describe the bug

I'm unable to create new environments in my workspace. When I try to create an environment with a `parentId`, I'm getting an error saying that the parentId is missing, even though I'm clearly providing it.

### Reproduction

```js
// Trying to create an environment with a parentId
const newEnv = create({
  parentId: 'wrk_123456',
  name: 'My Environment',
  data: {}
});

// Error: New Environment missing `parentId`: {"parentId":"wrk_123456","name":"My Environment","data":{}}
```

### Expected behavior

The environment should be created successfully when a valid `parentId` is provided. The error message suggests that `parentId` is required, but providing it causes the creation to fail.

### Additional context

This seems to have started recently. Previously I was able to create environments without issues. Now the validation logic appears to be inverted - it throws an error when `parentId` IS present instead of when it's missing.

---
Repository: /testbed
