# Bug Report

### Describe the bug

The `getDescription` method in `inputWrapperQueries` is returning an unexpected type. Instead of returning a single element like the other query methods (`getLabel`, `getError`, `getRequired`), it now returns a NodeList from `querySelectorAll`.

This breaks the consistency of the API and causes issues when trying to access the description element directly, since you now get a NodeList instead of an HTMLElement.

### Reproduction

```ts
import { inputWrapperQueries } from '@mantine-tests/core';

const container = document.createElement('div');
container.innerHTML = `
  <div class="mantine-InputWrapper-description">Test description</div>
`;

const description = inputWrapperQueries.getDescription(container);

// Expected: description to be an HTMLElement
// Actual: description is a NodeList

// This will fail because description is not an HTMLElement
console.log(description.textContent); // Error: Property 'textContent' does not exist on type 'NodeListOf<Element>'
```

### Expected behavior

The `getDescription` method should return a single HTMLElement (or null) like the other query methods in the same object:
- `getLabel` returns a single element
- `getError` returns a single element  
- `getRequired` returns a single element
- `getDescription` should also return a single element

The method signature should be consistent across all query methods.

### System Info
- Package: @mantine-tests/core
- Affected file: `packages/@mantine-tests/core/src/queries/input-wrapper.queries.ts`

---
Repository: /testbed
