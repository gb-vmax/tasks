# Bug Report

### Describe the bug

The `getLabel` query in InputWrapper is returning the error element instead of the label element. When trying to access the label of an input wrapper component, I'm getting the error message element instead.

### Reproduction

```tsx
import { render } from '@testing-library/react';
import { TextInput } from '@mantine/core';

const { container } = render(
  <TextInput
    label="Username"
    error="This field is required"
  />
);

// Trying to get the label
const label = container.querySelector('.mantine-InputWrapper-label');
// Expected: element with text "Username"
// Actual: element with text "This field is required" (the error)
```

When querying for the label element, the selector is pointing to `.mantine-InputWrapper-error` instead of `.mantine-InputWrapper-label`, so it returns the error element.

### Expected behavior

The label query should return the actual label element containing "Username", not the error element. These should be separate elements with different selectors.

### System Info
- @mantine/core: latest
- React: 18.x

---
Repository: /testbed
