# Bug Report

### Describe the bug

I'm experiencing an issue with the Slider component when using decimal step values. When I set a step value like `0.1` or `0.01`, the slider doesn't respect the precision and allows values that don't align with the specified step.

### Reproduction

```jsx
import { Slider } from '@mantine/core';

function Demo() {
  return (
    <Slider
      min={0}
      max={10}
      step={0.1}
      defaultValue={5}
    />
  );
}
```

When dragging the slider, instead of snapping to values like 5.0, 5.1, 5.2, etc., it produces values with incorrect precision like 5.123456789.

### Expected behavior

The slider should snap to values that match the step precision. With `step={0.1}`, values should be rounded to one decimal place (e.g., 5.1, 5.2, 5.3). With `step={0.01}`, values should be rounded to two decimal places.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
