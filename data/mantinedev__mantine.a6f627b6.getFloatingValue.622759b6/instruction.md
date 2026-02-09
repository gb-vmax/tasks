# Bug Report

### Describe the bug

The Slider component is not properly handling decimal values when precision is set. Instead of rounding to the specified precision, values are being floored, which causes the slider to always round down rather than to the nearest value.

### Reproduction

```js
import { Slider } from '@mantine/core';

// Example 1: Value should round to 2.35, but rounds down to 2.34
<Slider 
  value={2.345} 
  precision={2}
/>

// Example 2: Value should round to 1.68, but rounds down to 1.67
<Slider 
  value={1.678} 
  precision={2}
/>
```

When dragging the slider or setting values programmatically, numbers that should round up (e.g., 2.345 → 2.35) are instead being floored to the lower precision value (2.34).

### Expected behavior

The slider should round to the nearest value based on the precision, not always floor. For example:
- `2.345` with precision `2` should become `2.35` (not `2.34`)
- `1.678` with precision `2` should become `1.68` (not `1.67`)
- `0.125` with precision `2` should become `0.13` (not `0.12`)

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
