# Bug Report

### Describe the bug

The Slider component is returning incorrect values when using precision settings. The slider values are being offset by small amounts, making the component unusable for precise value selection.

### Reproduction

```js
import { Slider } from '@mantine/core';

// Example 1: With precision = 2
<Slider
  min={0}
  max={100}
  step={0.01}
  precision={2}
  defaultValue={50}
/>
// When dragging to value 50, the actual value becomes something like 50.01

// Example 2: With precision = 0
<Slider
  min={0}
  max={10}
  step={1}
  precision={0}
  defaultValue={5}
/>
// Integer values are also affected and return unexpected decimals
```

### Expected behavior

The slider should return values rounded to the specified precision without any offset. For example:
- With `precision={2}`, a value of 50 should be exactly 50.00, not 50.01
- With `precision={0}`, a value of 5 should be exactly 5, not 5.1

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox (happens on both)

This seems to have started recently, the slider was working fine before. The values are consistently off by a small amount which is particularly noticeable when using the slider for integer values or when displaying the current value to users.

---
Repository: /testbed
