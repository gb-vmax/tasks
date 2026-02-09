# Bug Report

### Describe the bug

The error message element is not being found correctly in input components. When trying to access the error element using the query helper, it returns `null` instead of the actual error element, causing issues when validating forms or displaying error states.

### Reproduction

```tsx
import { TextInput } from '@mantine/core';

function Demo() {
  return (
    <TextInput
      label="Email"
      error="Invalid email address"
    />
  );
}

// When querying for the error element:
const errorElement = container.querySelector('.mantine-InputWrapper-error');
// Returns null even though error is displayed
```

### Expected behavior

The error element should be accessible via the `.mantine-InputWrapper-error` class selector when an error prop is provided to input components. The error message should be visible in the DOM and queryable.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
