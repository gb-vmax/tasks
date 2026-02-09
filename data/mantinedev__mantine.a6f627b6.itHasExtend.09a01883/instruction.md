# Bug Report

### Describe the bug

The static `extend` function on components is not being recognized correctly. When checking the type of the `extend` property on a component, it appears to be an object instead of a function.

### Reproduction

```js
import { SomeComponent } from '@mantine/core';

// This check fails
console.log(typeof SomeComponent.extend); // Expected: 'function', Actual: 'object'
```

### Expected behavior

The `extend` property should be a function that can be called to extend component functionality. Currently it's returning as an object type which breaks the expected API.

### System Info
- @mantine/core version: latest
- Node version: 18.x

---
Repository: /testbed
