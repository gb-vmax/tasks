# Bug Report

### Describe the bug

The `getError` query in `inputWrapperQueries` is returning unexpected results when dealing with input wrappers that have multiple error elements. The logic seems to be incorrectly selecting error elements, causing issues when trying to access the actual error message.

### Reproduction

```tsx
import { inputWrapperQueries } from '@mantine-tests/core';

// Create a container with error elements
const container = document.createElement('div');
container.innerHTML = `
  <div class="mantine-InputWrapper-error">First error</div>
  <div class="mantine-InputWrapper-error"></div>
`;

// Try to get the error element
const error = inputWrapperQueries.getError(container);
console.log(error.textContent); // Expected: "First error", but behavior is inconsistent
```

### Expected behavior

The `getError` query should consistently return the first error element when multiple errors exist, or handle the case properly when error elements have no content.

### System Info

- @mantine/core version: latest
- Node version: 18.x

---
Repository: /testbed
