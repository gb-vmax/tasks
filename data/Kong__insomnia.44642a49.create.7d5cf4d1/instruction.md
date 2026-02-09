# Bug Report

### Describe the bug

I'm encountering an issue when trying to create a new CookieJar with a `parentId`. The creation fails with an error message saying the `parentId` is missing, but I'm actually providing it.

### Reproduction

```js
const newCookieJar = await create({
  parentId: 'wrk_123456',
  // other cookie jar properties
});
```

This throws an error:
```
Error: New CookieJar missing `parentId`: {"parentId":"wrk_123456",...}
```

### Expected behavior

The CookieJar should be created successfully when a valid `parentId` is provided. The error message doesn't make sense - it says the `parentId` is missing but it's clearly there in the JSON output.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
