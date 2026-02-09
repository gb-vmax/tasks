# Bug Report

### Describe the bug
When trying to create a new RequestMeta object, I'm getting an error thrown even when I provide a valid `parentId`. The error message says "New RequestMeta missing `parentId`" but I'm definitely passing it in.

### Reproduction
```js
const requestMeta = create({
  parentId: 'req_123',
  // other properties...
});
```

This throws an error:
```
Error: New RequestMeta missing `parentId` {"parentId":"req_123"}
```

### Expected behavior
The RequestMeta should be created successfully when a valid `parentId` is provided. The error should only be thrown when `parentId` is actually missing or undefined.

### Additional context
This seems to have broken recently - it was working fine before. Now it's impossible to create any new RequestMeta objects because the validation logic appears to be inverted.

---
Repository: /testbed
