# Bug Report

### Describe the bug

The `getFontSize` utility is returning incorrect CSS variable references. When I try to use font size props on components, the styles aren't being applied correctly and I'm seeing broken CSS variables in the rendered output.

### Reproduction

```tsx
import { Text } from '@mantine/core';

function Demo() {
  return (
    <Text size="md">
      This text should use the md font size
    </Text>
  );
}
```

When inspecting the rendered element, the CSS variable reference appears to be wrong. Instead of getting the expected `--mantine-font-size-md` variable, it seems like the component is trying to use a different variable name that doesn't exist in the theme.

### Expected behavior

The component should apply the correct font size using the proper CSS variable from the theme. Text with `size="md"` should render with `var(--mantine-font-size-md)`.

### Additional context

This seems to have broken recently. The font sizes were working fine before, but now all text components are rendering with incorrect or missing font size styles.

---
Repository: /testbed
