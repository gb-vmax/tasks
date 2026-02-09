# Bug Report

### Describe the bug

The `RingProgress` component is rendering incorrectly after a recent update. The ring segments appear to be sized wrong and don't properly fill the circular path. The visual appearance is off - the rings look either too thick or the gaps between segments are incorrect.

### Reproduction

```jsx
import { RingProgress } from '@mantine/core';

function Demo() {
  return (
    <RingProgress
      size={120}
      thickness={12}
      sections={[
        { value: 40, color: 'cyan' },
        { value: 25, color: 'orange' },
        { value: 15, color: 'grape' }
      ]}
    />
  );
}
```

When rendering this component, the ring segments don't appear to match the expected proportions. The curve calculations seem off.

### Expected behavior

The ring progress should render with properly proportioned segments that correctly fill the circular path based on the provided `size` and `thickness` values. The visual representation should match the percentage values given in the sections.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
