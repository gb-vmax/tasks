# Bug Report

### Describe the bug

The `jar()` method on `CookieObject` is returning a copy of the cookie jar instead of the original reference. This breaks functionality when trying to modify the cookie jar through the returned object.

### Reproduction

```js
const cookieObject = new CookieObject(/* ... */);
const jar = cookieObject.jar();

// Try to modify the jar
jar.someCookieProperty = 'newValue';

// The original cookieJar is not updated
console.log(cookieObject.cookieJar.someCookieProperty); // undefined
```

### Expected behavior

The `jar()` method should return a reference to the actual cookie jar object so that modifications to it are reflected in the original `cookieJar`. Previously this worked fine, but now it seems to be returning a shallow copy instead.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
