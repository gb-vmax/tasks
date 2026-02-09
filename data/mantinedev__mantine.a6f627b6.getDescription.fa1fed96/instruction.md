# Bug Report

### Describe the bug

The `getDescription` query in the input wrapper is returning the wrong element. Instead of selecting the description element with class `.mantine-InputWrapper-description`, it's now selecting the error element (`.mantine-InputWrapper-error`) or falling back to the container itself.

### Reproduction

```tsx
import { render } from '@testing-library/react';
import { TextInput } from '@mantine/core';

const { container } = render(
  <TextInput
    label="Test Input"
    description="This is a description"
    error="This is an error"
  />
);

// Try to get the description element
const description = container.querySelector('.mantine-InputWrapper-description');
console.log(description?.textContent); // Expected: "This is a description"

// But the getDescription query returns error element instead
const result = container.querySelector('.mantine-InputWrapper-error') || container;
console.log(result?.textContent); // Returns: "This is an error"
```

### Expected behavior

The `getDescription` query should return the element with class `.mantine-InputWrapper-description` that contains the description text, not the error element.

### System Info
- @mantine/core version: latest
- Browser: N/A (testing utilities)

---
Repository: /testbed
