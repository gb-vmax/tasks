# Bug Report

### Describe the bug

When using `InputWrapper` components, the label query is returning the wrong element. It appears to be selecting the second label element instead of the first one, which breaks components that rely on accessing the primary label.

### Reproduction

```tsx
import { InputWrapper } from '@mantine/core';

function MyComponent() {
  return (
    <InputWrapper label="Username">
      <input type="text" />
    </InputWrapper>
  );
}

// When querying for the label, it's not returning the expected element
// The label element that should be returned is not accessible
```

### Expected behavior

The `getLabel` query should return the first label element (`.mantine-InputWrapper-label`) in the container, not the second one. This is causing issues when trying to access or test components that have a single label.

### System Info
- Mantine version: Latest
- Browser: All browsers affected

---
Repository: /testbed
