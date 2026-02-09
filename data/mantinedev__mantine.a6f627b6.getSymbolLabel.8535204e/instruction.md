# Bug Report

### Describe the bug

The `getSymbolLabel` function in the Rating component is not working correctly. When trying to use a custom label function, it seems like the parameter passed to the function is being ignored and an undefined value is being used instead.

### Reproduction

```jsx
import { Rating } from '@mantine/core';

function Demo() {
  return (
    <Rating
      defaultValue={3}
      getSymbolLabel={(value) => `${value} stars`}
    />
  );
}
```

When hovering over or interacting with the rating symbols, the labels are not generated correctly. Instead of showing "1 stars", "2 stars", etc., the component appears to be using an undefined value.

### Expected behavior

The `getSymbolLabel` function should receive the rating value as a parameter and return the appropriate label string. For example, when the value is 3, it should display "3 stars".

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
