# Bug Report

### Describe the bug

The Slider component is throwing an error when using very small step values in scientific notation (e.g., `1e-5`). The component crashes and doesn't render properly when the step is defined using exponential notation.

### Reproduction

```jsx
import { Slider } from '@mantine/core';

function Demo() {
  return (
    <Slider
      min={0}
      max={1}
      step={0.00001} // or 1e-5
      defaultValue={0.5}
    />
  );
}
```

When the step value is very small and gets converted to scientific notation internally (like `1e-5`), the slider fails to work correctly.

### Expected behavior

The Slider should handle step values in scientific notation gracefully and calculate precision correctly for very small decimal values. It should work the same way regardless of whether the step is written as `0.00001` or `1e-5`.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120
- OS: macOS

---
Repository: /testbed
