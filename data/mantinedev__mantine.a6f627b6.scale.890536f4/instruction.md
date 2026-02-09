# Bug Report

### Describe the bug

I'm experiencing an issue with the RangeSlider component where the scale function is returning unexpected values. When using a custom scale function, I'm getting `NaN` or incorrect string values instead of the expected numeric values.

### Reproduction

```jsx
import { RangeSlider } from '@mantine/core';

function Demo() {
  return (
    <RangeSlider
      min={0}
      max={100}
      defaultValue={[20, 80]}
      scale={(v) => v * 2}
    />
  );
}
```

When moving the slider, the values seem to be processed incorrectly. The scale function should receive numeric values and return transformed numeric values, but something in the internal processing is causing issues.

### Expected behavior

The scale function should:
1. Receive numeric values from the slider
2. Apply the transformation
3. Return numeric values that are properly used by the component

The slider should work smoothly with custom scale functions without any unexpected type conversions or NaN values.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
