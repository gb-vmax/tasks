# Bug Report

### Describe the bug

When using the `inputWrapperQueries.getError()` helper function, it returns a `NodeList` instead of a single `HTMLElement`. This breaks code that expects a single error element and tries to access properties or methods directly on the returned value.

### Reproduction

```js
import { inputWrapperQueries } from '@mantine-tests/core';

const container = document.querySelector('.my-input-wrapper');
const error = inputWrapperQueries.getError(container);

// This will fail because error is now a NodeList, not an HTMLElement
error.textContent; // TypeError: Cannot read property 'textContent' of undefined
error.classList.add('custom-class'); // TypeError: error.classList is not a function
```

### Expected behavior

`getError()` should return a single `HTMLElement` (the first matching error element), consistent with the other query methods like `getLabel()`, `getRequired()`, and `getDescription()` which all use `querySelector()` and return single elements.

### System Info

- @mantine/core version: latest
- Framework: React

---
Repository: /testbed
