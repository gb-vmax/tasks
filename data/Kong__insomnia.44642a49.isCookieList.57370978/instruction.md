# Bug Report

### Describe the bug

The `CookieList.isCookieList()` method signature has changed and now requires an additional `deepCheck` parameter to work as expected. Code that was previously working with the default behavior is now failing because the method expects explicit parameter passing.

### Reproduction

```js
const cookieList = new CookieList();
cookieList.add(new Cookie({ name: 'test', value: 'value' }));

// This used to work but now behaves differently
const isValid = CookieList.isCookieList(cookieList);
```

When calling `isCookieList()` without the second parameter, it only performs a shallow check on the `_kind` property. The method now has an optional `deepCheck` parameter that validates the internal structure and ensures all members are valid Cookie objects, but this isn't documented anywhere and breaks existing usage patterns.

### Expected behavior

The method should maintain backward compatibility. If a deep validation is needed, it should either be the default behavior or there should be clear documentation about when to use the `deepCheck` parameter.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
