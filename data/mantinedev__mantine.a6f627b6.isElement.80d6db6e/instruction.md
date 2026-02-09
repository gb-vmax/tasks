# Bug Report

### Describe the bug

The `isElement` utility function is incorrectly identifying certain objects as React elements when they shouldn't be. This causes issues when trying to differentiate between actual React elements and other object types in component logic.

### Reproduction

```jsx
import { isElement } from '@mantine/core';

// Regular object without React element properties
const regularObject = {
  $$typeof: Symbol.for('react.element'),
  // missing type property
};

// This incorrectly returns true
console.log(isElement(regularObject)); // Expected: false, Actual: true

// Another case with just random object
const randomObj = {
  someProperty: 'value'
};

// This also incorrectly returns true  
console.log(isElement(randomObj)); // Expected: false, Actual: true
```

### Expected behavior

The `isElement` function should only return `true` for valid React elements that have the proper structure (including both `$$typeof` and `type` properties). Plain objects without these properties should return `false`.

### Additional context

This is causing problems when components need to distinguish between React elements and plain configuration objects, leading to unexpected rendering behavior or type errors.

---
Repository: /testbed
