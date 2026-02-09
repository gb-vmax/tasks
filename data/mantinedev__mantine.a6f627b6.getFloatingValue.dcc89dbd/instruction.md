# Bug Report

### Describe the bug

I'm experiencing incorrect rounding behavior with the Slider component when using specific precision values. The slider seems to be displaying and returning values that don't match the expected precision.

### Reproduction

```js
import { Slider } from '@mantine/core';

// Example 1: precision=2
<Slider
  min={0}
  max={100}
  step={0.01}
  precision={2}
  defaultValue={12.34}
/>
// When I interact with the slider, values like 12.34 are being displayed/returned as unexpected values

// Example 2: precision=1  
<Slider
  min={0}
  max={10}
  step={0.1}
  precision={1}
  defaultValue={5.5}
/>
// Similar issue - the value formatting doesn't seem right
```

### Expected behavior

The slider should respect the `precision` prop and format values correctly. For example:
- With `precision={2}`, a value of 12.34 should remain 12.34
- With `precision={1}`, a value of 5.5 should remain 5.5

Instead, the values seem to be formatted differently than expected.

### System Info

- @mantine/core version: latest
- Browser: Chrome
- OS: macOS

---
Repository: /testbed
