# Bug Report

### Slider position calculation incorrect

I'm experiencing an issue with the Slider component where the thumb position is not calculated correctly. The slider thumb appears in the wrong position relative to its actual value.

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

When the slider is set to a value of 50 with min=0 and max=100, the thumb should be positioned at 50% of the track width, but it appears in an incorrect position.

### Expected behavior

The slider thumb should be positioned proportionally to its value within the min/max range. For example:
- Value 0 (min) → thumb at 0% (left edge)
- Value 50 (middle) → thumb at 50% (center)
- Value 100 (max) → thumb at 100% (right edge)

### Additional context

This seems to affect all slider values, not just specific edge cases. The positioning formula appears to be calculating incorrectly.

---
Repository: /testbed
