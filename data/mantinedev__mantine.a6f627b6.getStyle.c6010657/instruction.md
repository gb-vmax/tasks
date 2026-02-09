# Bug Report

### Describe the bug

I'm experiencing an issue where custom styles passed through the `styles` prop are not being applied correctly to components. It seems like the styles are only being applied when they shouldn't be, or vice versa.

### Reproduction

```tsx
import { Button } from '@mantine/core';

function Demo() {
  return (
    <Button
      styles={{
        root: {
          backgroundColor: 'red',
        },
      }}
    >
      Click me
    </Button>
  );
}
```

When rendering this component, the custom background color doesn't appear on the button's root element. The styles seem to be completely ignored or applied to the wrong elements.

Similarly, when trying to style nested elements:

```tsx
<Button
  styles={{
    label: {
      fontSize: '20px',
    },
  }}
>
  Click me
</Button>
```

The label styles are not being applied as expected.

### Expected behavior

Custom styles passed through the `styles` prop should be correctly applied to the corresponding component elements (root, label, etc.). The component should render with the custom styles merged with the default theme styles.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
