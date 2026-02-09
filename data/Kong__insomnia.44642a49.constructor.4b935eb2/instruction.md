# Bug Report

### Describe the bug

I'm experiencing an issue where the SDK crashes when trying to work with property objects. It looks like the code is getting cut off or incomplete, causing runtime errors when trying to use methods on `PropertyBase` instances.

### Reproduction

```js
const property = new PropertyBase('test description');

// Trying to find properties in parent chain
const result = property.findInParents('someProperty');

// This throws an error because the method implementation is incomplete
```

### Expected behavior

The `PropertyBase` class methods should work correctly and not throw errors. Methods like `findInParents` should be able to traverse the parent chain and return the appropriate results.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

This seems to have started happening recently. The class definition appears to be truncated or corrupted somehow. Any help would be appreciated!

---
Repository: /testbed
