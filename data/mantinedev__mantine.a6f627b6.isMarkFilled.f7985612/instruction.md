# Bug Report

### Describe the bug

I'm experiencing an issue with the Slider component where marks are not being filled correctly in certain scenarios. The visual state of the marks doesn't match what I expect based on the slider's current value.

### Reproduction

```jsx
import { Slider } from '@mantine/core';

function Demo() {
  return (
    <Slider
      defaultValue={50}
      marks={[
        { value: 20, label: '20%' },
        { value: 50, label: '50%' },
        { value: 80, label: '80%' }
      ]}
    />
  );
}
```

When the slider value is exactly at a mark position (e.g., value = 50), the mark at that exact position should be filled, but it appears unfilled. This is particularly noticeable when:
1. Setting the slider to an exact mark value
2. The filled state of marks doesn't update correctly as you drag the slider

Also seeing similar issues with inverted sliders - the marks seem to fill in the opposite pattern than expected, or don't fill when they should.

### Expected behavior

- When the slider value equals a mark value, that mark should be filled
- Marks below the current value should be filled (or above for inverted sliders)
- The visual state should accurately reflect the slider position

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
