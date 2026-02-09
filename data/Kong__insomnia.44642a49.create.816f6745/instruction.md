# Bug Report

### Describe the bug

I'm encountering an issue when trying to create a new UnitTestSuite. The creation fails with an error even when I provide a valid `parentId` in the patch object.

### Reproduction

```js
// This throws an error unexpectedly
const suite = create({
  parentId: 'wrk_123',
  name: 'My Test Suite'
});
// Error: New UnitTestSuite missing `parentId` {"parentId":"wrk_123","name":"My Test Suite"}
```

### Expected behavior

The UnitTestSuite should be created successfully when a `parentId` is provided. The error message suggests that `parentId` is required, but providing it causes the creation to fail.

### Additional context

This seems backwards - the validation is rejecting valid input. I would expect:
- If `parentId` is provided → creation succeeds
- If `parentId` is missing → error is thrown

But currently it appears to be doing the opposite.

---
Repository: /testbed
