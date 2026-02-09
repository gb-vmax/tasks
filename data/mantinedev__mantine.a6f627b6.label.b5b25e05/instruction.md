# Bug Report

### Describe the bug

The RangeSlider component's default label formatter is now returning `undefined` for certain falsy values instead of displaying them. This breaks the expected behavior when trying to show labels for values like `0` (zero) or empty strings.

### Reproduction

```jsx
import { RangeSlider } from '@mantine/core';

function Demo() {
  return (
    <RangeSlider
      min={0}
      max={10}
      defaultValue={[0, 5]}
    />
  );
}
```

When the slider thumb is at position `0`, the label doesn't appear or shows as undefined instead of displaying "0".

This also affects cases where you might want to display an empty string as a label:

```jsx
<RangeSlider
  min={0}
  max={3}
  defaultValue={[0, 2]}
  label={(value) => ['', 'Low', 'Medium', 'High'][value]}
/>
```

The first position (empty string) doesn't render properly.

### Expected behavior

The label should display `0` when the slider value is zero, and should handle empty strings as valid label values. Previously, these falsy values were passed through correctly by the default label formatter.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
