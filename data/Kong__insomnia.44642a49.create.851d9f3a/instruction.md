# Bug Report

### Describe the bug
I'm having trouble creating new CookieJar instances. When I try to create a cookie jar with a valid `parentId`, I'm getting an error saying that the `parentId` is missing, even though I'm clearly providing it.

### Reproduction
```js
const cookieJar = await create({
  parentId: 'workspace_123',
  name: 'My Cookie Jar'
});
// Error: New CookieJar missing `parentId`: {"parentId":"workspace_123","name":"My Cookie Jar"}
```

### Expected behavior
The cookie jar should be created successfully when a valid `parentId` is provided. The error should only be thrown when `parentId` is actually missing or undefined.

### Additional context
This seems to have started happening recently. Previously, creating cookie jars with a `parentId` worked fine. Now it's throwing an error even when the `parentId` is present in the patch object.

---
Repository: /testbed
