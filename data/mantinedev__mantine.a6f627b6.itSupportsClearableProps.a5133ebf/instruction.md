# Bug Report

### Describe the bug

The clear button is not rendering when `clearable` prop is set to `true` and `rightSection` is provided. The clear button seems to be completely missing from the DOM even though the clearable functionality should take precedence over the custom right section.

### Reproduction

```tsx
import { DateInput } from '@mantine/dates';

function Demo() {
  return (
    <DateInput
      clearable
      clearButtonProps={{ 'aria-label': 'test-clear' }}
      rightSection="test-right-section"
    />
  );
}
```

When inspecting the DOM, the clear button with `aria-label="test-clear"` is not present. Only the custom right section content is rendered.

### Expected behavior

When `clearable` is set to `true`, the clear button should render in the right section, replacing any custom `rightSection` content. The clear button should be accessible via its aria-label.

Additionally, when passing `clearButtonProps` with custom attributes like `data-test-attr`, these attributes should be properly applied to the clear button element.

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
