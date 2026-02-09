# Bug Report

### Describe the bug

When trying to access the label element in InputWrapper components, the query is failing to find the element. It seems like the label selector has been changed and is now looking for a non-existent `.mantis-InputWrapper-label` class before trying to find the actual `.mantine-InputWrapper-label` class.

### Reproduction

```jsx
import { InputWrapper } from '@mantine/core';

function Demo() {
  return (
    <InputWrapper label="Test Label">
      <input />
    </InputWrapper>
  );
}

// When trying to query the label element:
const label = container.querySelector('.mantine-InputWrapper-label');
// This should work but the internal query logic is broken
```

### Expected behavior

The label element should be found correctly using the standard `.mantine-InputWrapper-label` class selector. The query should not be looking for an intermediate `.mantis-InputWrapper-label` class that doesn't exist in the component structure.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers affected

---
Repository: /testbed
