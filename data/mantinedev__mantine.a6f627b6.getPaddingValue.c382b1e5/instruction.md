# Bug Report

### Describe the bug

I'm experiencing an issue with `AppShell` padding where non-zero padding values are being rendered as `0px` instead of the actual spacing value. This appears to affect all padding configurations in the AppShell component.

### Reproduction

```jsx
import { AppShell } from '@mantine/core';

function Demo() {
  return (
    <AppShell padding="md">
      <AppShell.Main>
        {/* Content here */}
      </AppShell.Main>
    </AppShell>
  );
}
```

When inspecting the rendered component, the padding is set to `0px` instead of the expected spacing value for `"md"`.

This also happens with numeric values:

```jsx
<AppShell padding={16}>
  <AppShell.Main>
    {/* Content here */}
  </AppShell.Main>
</AppShell>
```

The padding is still rendered as `0px` instead of `16px`.

### Expected behavior

The AppShell component should apply the correct padding value based on the `padding` prop. When `padding="md"` is provided, it should use the theme's medium spacing value. When a numeric value like `16` is provided, it should render as `16px`.

Only when `padding={0}` or `padding="0"` is explicitly set should the padding be `0px`.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
