# Bug Report

### Describe the bug

Components are failing the `itHasClasses` validation check even when they have properly defined static classes. The test is incorrectly rejecting valid class objects.

### Reproduction

```tsx
import { itHasClasses } from '@mantine-tests/core';

// Component with valid classes object
const MyComponent = {
  classes: {
    root: 'my-component-root',
    label: 'my-component-label'
  }
};

// This test now fails unexpectedly
itHasClasses({ component: MyComponent });
```

### Expected behavior

The test should pass when a component has a valid `classes` object (non-null object that is not an array). Components with properly structured static classes are being rejected by the validation.

### System Info
- @mantine/core: latest
- React: 18.x

---
Repository: /testbed
