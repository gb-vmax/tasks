# Bug Report

### Describe the bug

The Slider component is not handling decimal step values correctly. When using a step value with decimal places, the precision calculation appears to be off, causing the slider to snap to incorrect values or display wrong decimal precision.

### Reproduction

```js
import { Slider } from '@mantine/core';

// Using a slider with decimal step
<Slider 
  min={0} 
  max={10} 
  step={0.1} 
  defaultValue={5} 
/>
```

When dragging the slider or using keyboard controls, the values don't align properly with the expected 0.1 increments. For example, trying to set a value like 5.5 might result in unexpected behavior or incorrect rounding.

### Expected behavior

The slider should respect the decimal precision of the step value and snap to correct increments (e.g., 5.0, 5.1, 5.2, etc. when step is 0.1).

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
