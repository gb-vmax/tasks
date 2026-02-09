# Bug Report

### Describe the bug

The Slider component is displaying values in reverse - when I set a value closer to the maximum, the thumb appears closer to the minimum position, and vice versa. The visual position of the slider thumb doesn't match the actual value.

### Reproduction

```jsx
import { Slider } from '@mantine/core';

function Demo() {
  return (
    <Slider
      min={0}
      max={100}
      defaultValue={25}
    />
  );
}
```

When setting `defaultValue={25}`, the thumb appears at the 75% position instead of 25%.
When setting `defaultValue={75}`, the thumb appears at the 25% position instead of 75%.

### Expected behavior

The slider thumb should be positioned at 25% from the left when the value is 25, and at 75% from the left when the value is 75. The visual position should directly correspond to the value relative to the min/max range.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
