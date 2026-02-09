# Bug Report

### Describe the bug

When using the Slider component with a value of `0`, the slider thumb doesn't render at the correct position. The slider appears to be broken when the value is exactly zero, but works fine with any other value including negative numbers.

### Reproduction

```jsx
import { Slider } from '@mantine/core';

function Demo() {
  return (
    <Slider
      value={0}
      min={-10}
      max={10}
    />
  );
}
```

### Expected behavior

The slider thumb should be positioned correctly when the value is `0`. Currently, it seems like the value of `0` is being treated differently than other values, causing the thumb to not display or position properly.

### Additional context

- This also affects controlled sliders where the value can be set to `0` programmatically
- Negative values seem to work fine
- Positive values work as expected
- Only the exact value of `0` causes issues

---
Repository: /testbed
