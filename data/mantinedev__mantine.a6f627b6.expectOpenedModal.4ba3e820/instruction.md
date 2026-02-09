# Bug Report

### Describe the bug

When using date input components with modal mode, the modal detection helper is not working correctly. The `expectOpenedModal` function appears to be checking for the wrong condition - it's verifying that the modal is NOT present when it should be verifying that it IS present.

### Reproduction

```jsx
import { DateInput } from '@mantine/dates';
import { expectOpenedModal } from '@mantine-tests/dates';

function MyComponent() {
  return (
    <DateInput
      modal
      popoverProps={{ opened: true }}
      label="Pick date"
    />
  );
}

// Test the modal state
const { container } = render(<MyComponent />);
expectOpenedModal(container); // This fails even when modal is visible
```

### Expected behavior

The `expectOpenedModal` helper should correctly detect when a modal is open. Currently it seems to be checking for the absence of the modal instead of its presence, which causes false negatives when the modal is actually displayed.

### System Info
- @mantine/dates version: latest
- @mantine/core version: latest

---
Repository: /testbed
