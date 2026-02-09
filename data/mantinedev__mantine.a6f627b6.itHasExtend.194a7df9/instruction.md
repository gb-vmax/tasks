# Bug Report

### Describe the bug

The `itHasExtend` test helper is not working correctly. When I try to use it to verify that a component has a static `extend` function, the test fails unexpectedly.

### Reproduction

```tsx
import { itHasExtend } from '@mantine-tests/core';
import { MyComponent } from './MyComponent';

itHasExtend({ component: MyComponent });
```

The test fails even though `MyComponent` has a valid static `extend` function defined.

### Expected behavior

The test should pass when a component has a static `extend` function. The helper should check that `component.extend` is a function, not something else.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
