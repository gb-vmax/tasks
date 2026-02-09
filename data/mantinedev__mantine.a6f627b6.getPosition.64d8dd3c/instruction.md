# Bug Report

### Describe the bug

The Slider component is displaying incorrect thumb positions when values are set. The thumb position calculation seems to be wrong, especially noticeable when using sliders with different min/max ranges.

### Reproduction

```jsx
import { Slider } from '@mantine/core';

function Demo() {
  return (
    <>
      {/* Slider with range 0-100 */}
      <Slider value={50} min={0} max={100} />
      
      {/* Slider with range 10-90 */}
      <Slider value={50} min={10} max={90} />
      
      {/* Slider with negative range */}
      <Slider value={0} min={-50} max={50} />
    </>
  );
}
```

### Expected behavior

The slider thumb should be positioned correctly based on the value relative to the min/max range. For example:
- A value of 50 in a 0-100 range should position the thumb at 50%
- A value of 50 in a 10-90 range should position the thumb at 50%
- A value of 0 in a -50 to 50 range should position the thumb at 50%

### Actual behavior

The thumb positions are completely off. The calculations don't seem to respect the proper min/max range, causing thumbs to appear in unexpected positions or even outside the slider track bounds.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
