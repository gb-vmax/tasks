# Bug Report

### Describe the bug

I'm experiencing an issue with the `PropertyBase` class where methods are getting truncated or not properly defined. When trying to use parent-related methods like `findInParents()`, the code seems to be incomplete and doesn't execute as expected.

### Reproduction

```js
import { PropertyBase } from '@insomnia/sdk';

const property = new PropertyBase('test');
const parent = new PropertyBase('parent');
property._parent = parent;

// This doesn't work correctly
const result = property.findInParents('someProperty');
// Expected to traverse parent hierarchy but behavior is broken
```

### Expected behavior

The `findInParents()` method should properly traverse the parent hierarchy and return the appropriate ancestor when a property is found. The method should complete its logic and handle both cases where a customizer function is provided or not.

### System Info
- Package: @insomnia/sdk
- Node version: Latest

---
Repository: /testbed
