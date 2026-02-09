# Bug Report

### Describe the bug

When passing `null` as a shadow value, the component doesn't render correctly. It seems like `null` is being treated differently than expected and causes the shadow utility to return an unexpected result instead of properly handling the null case.

### Reproduction

```js
import { getShadow } from '@mantine/core';

// This should handle null gracefully
const shadow = getShadow(null);
console.log(shadow); // Returns unexpected value

// Works fine with undefined
const shadow2 = getShadow(undefined);
console.log(shadow2); // undefined (as expected)
```

When using components with `shadow={null}`, the behavior is inconsistent with other falsy values like `undefined`.

### Expected behavior

Passing `null` as a shadow value should be handled the same way as `undefined` - it should not apply any shadow styling. Currently it seems to be processed differently which causes rendering issues.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
