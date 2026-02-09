# Bug Report

### Describe the bug

I'm encountering an issue when trying to create a new CookieJar. The creation fails with an error message saying that `parentId` is missing, but I'm definitely passing it in the patch object.

### Reproduction

```js
const patch = {
  parentId: 'wrk_123456',
  // other cookie jar properties
};

await create(patch);
// Error: New CookieJar missing `parentId`: {"parentId":"wrk_123456",...}
```

### Expected behavior

The CookieJar should be created successfully when a valid `parentId` is provided in the patch object. The error should only be thrown when `parentId` is actually missing or undefined.

### Additional context

This seems to have broken recently. The error message is confusing because it shows that `parentId` is actually present in the patch object, yet it still throws the error about it being missing.

---
Repository: /testbed
