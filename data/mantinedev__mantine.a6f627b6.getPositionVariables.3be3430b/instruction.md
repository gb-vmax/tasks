# Bug Report

### Describe the bug

The `Indicator` component is not positioning correctly when using `middle` and `center` placements. The indicator appears in the wrong location on the screen instead of being centered on the target element.

### Reproduction

```jsx
import { Indicator } from '@mantine/core';

// Middle position - indicator is offset incorrectly
<Indicator position="middle-start">
  <div>Content</div>
</Indicator>

// Center placement - indicator appears on wrong side
<Indicator position="top-center">
  <div>Content</div>
</Indicator>
```

### Expected behavior

- When using `position="middle-*"`, the indicator should be vertically centered on the target element
- When using `position="*-center"`, the indicator should be horizontally centered on the target element

### Current behavior

The indicator is positioned incorrectly - it appears offset from where it should be. For middle positioning, it seems to be shifted in the wrong direction vertically. For center placement, it's appearing on the opposite side horizontally.

### System Info

- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
