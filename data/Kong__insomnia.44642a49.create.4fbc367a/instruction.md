# Bug Report

### Describe the bug

I'm encountering an issue when trying to create a new ProtoDirectory. The creation fails with an error message saying "New ProtoDirectory missing `parentId`" even when I'm providing a valid parentId in the patch object.

### Reproduction

```js
const newProtoDir = create({
  parentId: 'wrk_123456',
  name: 'my-proto-directory'
});
```

This throws an error: `New ProtoDirectory missing 'parentId'`

### Expected behavior

The ProtoDirectory should be created successfully when a valid parentId is provided. The validation should only throw an error when parentId is actually missing or undefined, not when it's present.

### Additional context

This seems to have broken recently - I was able to create proto directories without issues before. Now every attempt to create one with a parentId fails the validation check.

---
Repository: /testbed
