# Bug Report

### Describe the bug

The RingProgress component is rendering incorrectly after a recent update. The ring thickness appears to be calculated wrong, making the rings look much thicker than they should be. Also, when providing a `value` prop along with `root`, the stroke dash array seems to be calculated incorrectly and the visual representation doesn't match what's expected.

### Reproduction

```jsx
import { RingProgress } from '@mantine/core';

function Demo() {
  return (
    <RingProgress
      size={120}
      thickness={8}
      sections={[
        { value: 40, color: 'cyan' },
        { value: 25, color: 'orange' },
        { value: 15, color: 'grape' }
      ]}
    />
  );
}
```

The rings appear much thicker than the specified `thickness={8}` value. It looks like the radius calculation might be off.

Also, when using the `root` prop with a `value`:

```jsx
<RingProgress
  size={120}
  thickness={8}
  sections={[
    { value: 50, color: 'blue', root: true }
  ]}
/>
```

The ring doesn't render properly - it seems like the condition for determining the stroke dash array changed and now both `root` AND `value` being undefined is required instead of either one.

### Expected behavior

- Ring thickness should match the `thickness` prop value
- When `root` is true, the stroke dash array should be calculated based on the sum, regardless of whether `value` is provided

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
