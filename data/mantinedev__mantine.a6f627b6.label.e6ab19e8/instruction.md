# Bug Report

### Describe the bug

The Slider component's label is now displaying "undefined" as text when the value is 0 or other falsy values. Previously, the label would correctly show "0" for zero values, but after a recent change it's rendering the string "undefined" instead.

### Reproduction

```jsx
import { Slider } from '@mantine/core';

function Demo() {
  return (
    <Slider
      defaultValue={0}
      min={0}
      max={100}
    />
  );
}
```

When the slider is at position 0, the label displays "undefined" instead of "0".

This also affects any other falsy values that should be valid labels (like empty strings or the number 0).

### Expected behavior

The slider label should display "0" when the value is 0. Falsy values that are valid numbers or strings should be rendered correctly, not converted to "undefined".

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
