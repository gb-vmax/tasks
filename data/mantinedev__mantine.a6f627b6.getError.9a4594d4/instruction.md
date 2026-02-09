# Bug Report

### Describe the bug

After a recent update, the `getError` query in `inputWrapperQueries` is returning `undefined` instead of the error element. This is breaking error message display in my form validation.

### Reproduction

```tsx
import { render } from '@testing-library/react';
import { TextInput } from '@mantine/core';

const { container } = render(
  <TextInput
    label="Email"
    error="Invalid email address"
  />
);

// This now returns undefined
const errorElement = container.querySelector('.mantine-InputWrapper-error');
console.log(errorElement); // Expected: HTMLElement, Actual: undefined
```

The error element exists in the DOM but the query can't find it anymore. It seems like the query is looking for a specific attribute that may not be present on all error elements.

### Expected behavior

The `getError` query should return the error element when an error prop is passed to the input component, regardless of validation state.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
