# Bug Report

### Describe the bug

I'm experiencing an issue with the `getLabel` query in the InputWrapper component. When trying to access the label element, I'm getting unexpected behavior - it seems like the query is returning a collection instead of a single element, which is causing type errors and runtime issues in my tests.

### Reproduction

```tsx
import { inputWrapperQueries } from '@mantine-tests/core';

const container = document.createElement('div');
container.innerHTML = `
  <div class="mantine-InputWrapper-label">Label text</div>
`;

const label = inputWrapperQueries.getLabel(container);
// Expected: single HTMLElement
// Actual: returns NodeList or similar collection type
```

When I try to use the returned value as a single element (e.g., accessing `.textContent` or other DOM properties), it doesn't work as expected.

### Expected behavior

The `getLabel` method should return a single label element that can be used directly, consistent with how other query methods in the InputWrapper work (like `getError` and `getRequired`).

### System Info

- Mantine version: latest
- TypeScript version: 5.x

---
Repository: /testbed
