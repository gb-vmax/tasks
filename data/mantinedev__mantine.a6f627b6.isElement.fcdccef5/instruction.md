# Bug Report

### Describe the bug

I'm encountering an issue where React Fragments are being incorrectly treated as valid elements in certain scenarios. When passing a Fragment to a component that uses element validation, it's not being properly filtered out as expected.

### Reproduction

```jsx
import { Fragment } from 'react';

const element = <Fragment><div>Test</div></Fragment>;

// Fragment is incorrectly identified as a valid element
// Expected: false
// Actual: true (or unexpected behavior)
```

When I pass a Fragment to components that rely on element type checking, the validation doesn't work as it should. The Fragment passes through when it should be rejected.

### Expected behavior

Fragments should be properly identified and return `false` during element validation checks, similar to how `null` and arrays are handled.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Node version: 20.x

---
Repository: /testbed
