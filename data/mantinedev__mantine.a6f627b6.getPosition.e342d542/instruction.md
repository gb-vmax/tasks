# Bug Report

### Slider thumb position is completely wrong

I'm experiencing a really strange issue with the Slider component where the thumb position is completely inverted and doesn't match the actual value at all.

### Reproduction

```jsx
import { Slider } from '@mantine/core';

function Demo() {
  return (
    <Slider
      min={0}
      max={100}
      defaultValue={50}
    />
  );
}
```

When I set the slider to value 50 (middle), the thumb appears at the wrong position. The calculation seems completely off - as I move the slider, the thumb jumps around in unexpected ways instead of moving smoothly from left to right.

### Expected behavior

The slider thumb should be positioned at 50% when the value is 50 (with min=0 and max=100). More generally, the thumb position should accurately reflect the value relative to the min/max range.

For example:
- value=0 → thumb at 0%
- value=50 → thumb at 50%  
- value=100 → thumb at 100%

### System Info
- @mantine/core version: latest
- Browser: Chrome

This makes the Slider component completely unusable right now. Any help would be appreciated!

---
Repository: /testbed
