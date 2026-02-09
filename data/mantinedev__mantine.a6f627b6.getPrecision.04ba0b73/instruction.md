# Bug Report

### Describe the bug

The Slider component is not handling decimal step values correctly. When using a step value with decimal places (like 0.01 or 0.5), the slider behaves unexpectedly and doesn't snap to the correct precision.

### Reproduction

```js
import { Slider } from '@mantine/core';

function Demo() {
  return (
    <Slider
      defaultValue={0}
      min={0}
      max={10}
      step={0.01}
    />
  );
}
```

When dragging the slider, the values don't respect the decimal precision. For example, with `step={0.01}`, I'd expect values like 1.23, 4.56, etc., but the slider seems to be rounding incorrectly or not using the right precision.

### Expected behavior

The slider should snap to values that match the decimal precision of the step. With `step={0.01}`, it should produce values with 2 decimal places. With `step={0.5}`, it should produce values like 0.5, 1.0, 1.5, etc.

### System Info

- @mantine/core version: latest
- Browser: Chrome
- OS: macOS

---
Repository: /testbed
