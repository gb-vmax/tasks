# Bug Report

### Describe the bug

I'm experiencing an issue with the Slider component where marks at the exact current value position are not being filled/highlighted correctly. It seems like marks that should be considered "filled" when they match the slider's current value are being excluded.

### Reproduction

```jsx
import { Slider } from '@mantine/core';

function Demo() {
  return (
    <Slider
      defaultValue={50}
      marks={[
        { value: 0, label: '0' },
        { value: 25, label: '25' },
        { value: 50, label: '50' },
        { value: 75, label: '75' },
        { value: 100, label: '100' },
      ]}
    />
  );
}
```

When the slider value is exactly 50, the mark at position 50 doesn't get filled/highlighted. Same behavior happens with other values - if I set the slider to 25, the mark at 25 isn't filled either.

### Expected behavior

Marks at the current slider value position should be filled/highlighted along with all marks below that value (or above for inverted sliders). When the slider is at value 50, marks at 0, 25, and 50 should all be filled.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
