# Bug Report

### Describe the bug

The `clearable` prop is not working as expected in date picker components. When setting `clearable={false}`, the clear button still appears in the input. Additionally, props passed to `clearButtonProps` seem to be applied even when the clear button shouldn't be rendered.

### Reproduction

```tsx
import { DatePickerInput } from '@mantine/dates';

function Demo() {
  return (
    <DatePickerInput
      clearable={false}
      clearButtonProps={{ 'aria-label': 'clear-button' }}
      rightSection={<span>Custom icon</span>}
    />
  );
}
```

When `clearable` is set to `false`, the clear button should not be rendered at all. However, it appears that the button is still being added to the DOM.

### Expected behavior

- When `clearable={false}`, no clear button should be rendered
- When `clearable={false}`, the `clearButtonProps` should be ignored since there's no button to apply them to
- The `rightSection` should be visible regardless of the `clearable` prop value

### System Info

- @mantine/dates version: latest
- @mantine/core version: latest

---
Repository: /testbed
