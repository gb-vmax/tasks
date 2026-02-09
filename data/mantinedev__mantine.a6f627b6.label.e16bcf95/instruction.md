# Bug Report

### Describe the bug

The Slider component is not displaying labels for the thumb value anymore. When hovering over the slider or dragging it, the label that should show the current value is not appearing.

### Reproduction

```jsx
import { Slider } from '@mantine/core';

function Demo() {
  return (
    <Slider
      defaultValue={50}
      min={0}
      max={100}
    />
  );
}
```

When hovering over or dragging the slider, no label is shown even though `showLabelOnHover` is true by default.

Also tried with explicit label formatting:

```jsx
<Slider
  defaultValue={50}
  label={(value) => `${value}°C`}
  showLabelOnHover={true}
/>
```

Still no label appears.

### Expected behavior

The slider should display a label showing the current value when hovering over or dragging the thumb. The label should be formatted according to the `label` prop function (or use the default formatting if not provided).

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
