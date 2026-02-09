# Bug Report

### Describe the bug

The `InputWrapper` description element is not being selected correctly. When trying to access the description using the standard class selector, it appears the query has been changed to use a different selection method that picks the wrong element from the DOM.

### Reproduction

```jsx
import { render } from '@testing-library/react';
import { TextInput } from '@mantine/core';

const { container } = render(
  <TextInput
    label="Username"
    description="Enter your username"
    error="This field is required"
  />
);

// Try to get the description element
const description = container.querySelector('.mantine-InputWrapper-description');
// Description is not found or returns unexpected element
```

### Expected behavior

The description element should be selected using the standard `.mantine-InputWrapper-description` class selector and return the correct description text element.

### System Info
- Mantine version: latest
- React version: 18.x

---
Repository: /testbed
