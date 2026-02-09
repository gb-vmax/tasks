# Bug Report

### Describe the bug

The RingProgress component is rendering sections in the wrong order/position. The segments appear to be stacked incorrectly, with each section starting at the wrong offset position on the ring.

### Reproduction

```jsx
import { RingProgress } from '@mantine/core';

function Demo() {
  return (
    <RingProgress
      sections={[
        { value: 40, color: 'cyan' },
        { value: 25, color: 'orange' },
        { value: 15, color: 'grape' }
      ]}
    />
  );
}
```

When rendering this component, the sections don't appear in the correct positions around the ring. Instead of each section following the previous one, they seem to be positioned incorrectly.

### Expected behavior

Each section should be positioned sequentially around the ring, with the first section starting at the top and subsequent sections following in order. The offset calculation should properly account for the accumulated values of previous sections.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
