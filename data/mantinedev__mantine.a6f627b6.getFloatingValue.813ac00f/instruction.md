# Bug Report

### Describe the bug

I'm experiencing an issue with the Slider component where the displayed values have incorrect precision. When setting a specific `precision` prop, the slider shows values with one more decimal place than expected.

### Reproduction

```jsx
import { Slider } from '@mantine/core';

function Demo() {
  return (
    <Slider
      defaultValue={5.5}
      min={0}
      max={10}
      step={0.1}
      precision={1}
    />
  );
}
```

When dragging the slider, values are displayed with 2 decimal places (e.g., `5.55`) instead of 1 decimal place (e.g., `5.5`) as specified by the `precision={1}` prop.

### Expected behavior

The slider should respect the `precision` prop and display values with exactly the number of decimal places specified. For example:
- `precision={1}` should show values like `5.5`, `6.3`, etc.
- `precision={2}` should show values like `5.55`, `6.32`, etc.

Currently it seems like the precision is being increased by 1, showing an extra decimal place beyond what was configured.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
