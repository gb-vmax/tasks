# Bug Report

### Describe the bug

The RangeSlider component is not displaying labels correctly. When dragging the slider thumbs, the label tooltips appear empty instead of showing the current value.

### Reproduction

```jsx
import { RangeSlider } from '@mantine/core';

function Demo() {
  return (
    <RangeSlider
      defaultValue={[20, 80]}
      min={0}
      max={100}
    />
  );
}
```

### Steps to reproduce
1. Create a RangeSlider component with default props
2. Drag one of the thumbs
3. Observe that the label tooltip appears but shows nothing

### Expected behavior

The label should display the current numeric value of the slider thumb position (e.g., "20", "50", "80").

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
