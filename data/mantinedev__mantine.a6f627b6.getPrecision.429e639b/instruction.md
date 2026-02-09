# Bug Report

### Describe the bug

The Slider component is not handling decimal step values correctly. When I set a step value like `0.01` or `0.1`, the slider doesn't snap to the expected precision and the values are off.

### Reproduction

```jsx
import { Slider } from '@mantine/core';

function Demo() {
  return (
    <Slider
      min={0}
      max={1}
      step={0.01}
      defaultValue={0.5}
    />
  );
}
```

When dragging the slider, the values don't align properly to the 0.01 step increments. For example, instead of getting values like 0.01, 0.02, 0.03, I'm getting imprecise values.

### Expected behavior

The slider should respect the decimal precision of the step prop. With `step={0.01}`, values should be rounded to 2 decimal places. With `step={0.1}`, values should be rounded to 1 decimal place.

### System Info

- @mantine/core version: latest
- Browser: Chrome 120
- OS: macOS

---
Repository: /testbed
