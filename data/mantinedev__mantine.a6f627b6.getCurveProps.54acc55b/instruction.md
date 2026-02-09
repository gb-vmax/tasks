# Bug Report

### Describe the bug

The RingProgress component is rendering incorrectly - the progress segments appear inverted and the ring thickness/radius calculation seems off. The visual appearance doesn't match what's expected based on the provided values.

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
      ]}
    />
  );
}
```

### Expected behavior

The ring should display:
- A 40% cyan segment followed by a 25% orange segment
- Proper spacing/thickness based on the size and thickness props
- The filled portions should represent the actual percentage values

### Actual behavior

The progress segments appear to be inverted (empty space where filled should be, filled where empty should be). Additionally, the ring appears thinner than expected given the thickness prop, suggesting the radius calculation might be incorrect.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
