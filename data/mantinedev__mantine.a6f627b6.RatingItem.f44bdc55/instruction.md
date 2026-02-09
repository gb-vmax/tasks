# Bug Report

### Describe the bug

The Rating component is not rendering correctly - the input elements are showing up when they shouldn't be, and the fractional star display is completely inverted. When the component is in readOnly mode, interactive input fields are being rendered, which doesn't make sense. Additionally, the visual display of fractional ratings (like 3.5 stars) is backwards - empty stars are being shown as filled and vice versa.

### Reproduction

```jsx
import { Rating } from '@mantine/core';

// Case 1: ReadOnly mode showing inputs
<Rating value={3} readOnly />
// Expected: No input elements should be rendered
// Actual: Input elements are present in the DOM

// Case 2: Fractional rating display inverted
<Rating value={3.5} fractionValue={0.5} />
// Expected: 3 full stars + 1 half-filled star
// Actual: The half-filled star appears inverted (showing the wrong half)

// Case 3: Active state affecting clip-path incorrectly
<Rating value={2.7} />
// The fractional part of the rating is clipped in the opposite direction
```

### Expected behavior

1. When `readOnly` is true, no input elements should be rendered in the DOM
2. Fractional ratings should display the correct portion of each star as filled
3. The clip-path calculation should correctly show the filled portion based on the `fractionValue`

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
