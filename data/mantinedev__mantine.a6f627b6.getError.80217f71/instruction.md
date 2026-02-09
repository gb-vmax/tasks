# Bug Report

### Describe the bug

The error message element is not being found correctly in InputWrapper components. When trying to query for error messages, the selector is looking for `.mantine-InputWrapper-errors` (plural) but seems to fall back to `container.firstElementChild` if not found, which can return incorrect elements.

### Reproduction

```jsx
import { InputWrapper } from '@mantine/core';

function Demo() {
  return (
    <InputWrapper
      label="Input label"
      error="This is an error message"
    >
      <input />
    </InputWrapper>
  );
}
```

When trying to access the error element using the query helper:
```js
const errorElement = inputWrapperQueries.getError(container);
// Returns wrong element or undefined
```

### Expected behavior

The error query should correctly locate the error message element using the proper class name `.mantine-InputWrapper-error` (singular). The current implementation searches for `.mantine-InputWrapper-errors` (plural) which doesn't match the actual class name used in the component.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
