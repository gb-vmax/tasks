# Bug Report

### Describe the bug

The Slider component is displaying values in reverse - when I set a value closer to the maximum, the thumb appears closer to the minimum position, and vice versa. The visual position of the slider thumb doesn't match the actual value it represents.

### Reproduction

```jsx
import { Slider } from '@mantine/core';

function Demo() {
  return (
    <Slider
      min={0}
      max={100}
      defaultValue={75}
    />
  );
}
```

When setting `defaultValue={75}`, the thumb appears at the 25% position instead of 75%. Similarly, `defaultValue={25}` shows the thumb at 75%.

### Expected behavior

The slider thumb should be positioned at 75% from the left when the value is 75 (with min=0 and max=100). The visual position should directly correspond to the value - higher values should appear further to the right, and lower values should appear further to the left.

### Additional context

This seems to have started happening recently. The slider was working correctly before where the thumb position matched the actual value.

---
Repository: /testbed
