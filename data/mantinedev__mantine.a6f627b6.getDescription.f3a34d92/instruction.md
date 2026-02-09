# Bug Report

### Describe the bug
The `getDescription` query is returning the error element instead of the description element. When trying to access the description text of an input wrapper, it returns the error message content instead.

### Reproduction
```tsx
import { render } from '@testing-library/react';
import { TextInput } from '@mantine/core';

const { container } = render(
  <TextInput
    label="Username"
    description="Enter your username"
    error="This field is required"
  />
);

const description = container.querySelector('.mantine-InputWrapper-description');
const error = container.querySelector('.mantine-InputWrapper-error');

// description should contain "Enter your username"
// error should contain "This field is required"
// But getDescription query would return the error element instead
```

### Expected behavior
The `getDescription` query should return the element with class `mantine-InputWrapper-description`, not the error element. Description and error are separate parts of the input wrapper and should be queried independently.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
