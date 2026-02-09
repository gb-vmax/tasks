# Bug Report

### Describe the bug
When accessing the cookie jar through the `jar()` method, modifications to the returned object are unexpectedly persisting across subsequent calls. It seems like the method is returning a reference that allows external code to mutate the internal cookie jar state.

### Reproduction
```js
const cookieObj = new CookieObject(/* ... */);

// Get the jar
const jar1 = cookieObj.jar();
jar1.someProp = 'modified';

// Get the jar again
const jar2 = cookieObj.jar();

// jar2.someProp is 'modified' when it shouldn't be
// Expected jar2 to be independent of jar1
```

### Expected behavior
Each call to `jar()` should return an independent object that doesn't affect the internal state or other calls to `jar()`. Modifying the returned jar should not persist across multiple invocations.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
