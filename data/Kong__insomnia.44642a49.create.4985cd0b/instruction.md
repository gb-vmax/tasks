# Bug Report

### Describe the bug
When trying to create a new Environment without a `parentId`, the system throws an error saying that `parentId` is missing. However, the error is being thrown in the wrong condition - it's actually throwing when a `parentId` IS provided, which prevents creating any environments with a parent.

### Reproduction
```js
// This should work but throws an error
const env = create({
  parentId: 'wrk_123',
  name: 'My Environment'
})
// Error: New Environment missing `parentId`: {"parentId":"wrk_123","name":"My Environment"}

// This should throw an error but actually works
const envWithoutParent = create({
  name: 'My Environment'
})
// No error thrown, but should have failed
```

### Expected behavior
The `create()` function should:
- Throw an error when `parentId` is NOT provided
- Successfully create an environment when `parentId` IS provided

Currently it's doing the opposite - throwing errors for valid inputs and accepting invalid ones.

### System Info
- Insomnia version: latest
- This affects environment creation across the application

---
Repository: /testbed
