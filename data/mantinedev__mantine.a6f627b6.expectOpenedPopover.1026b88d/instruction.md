# Bug Report

### Describe the bug

The date picker popover is not being detected correctly after opening. When clicking on a date input field, the popover appears visually but the test helper function `expectOpenedPopover` fails to verify its presence.

### Reproduction

```tsx
import { render } from '@testing-library/react';
import { DateInput } from '@mantine/dates';
import { clickInput, expectOpenedPopover } from '@mantine-tests/dates';

const { container } = render(<DateInput />);
clickInput(container);

// This fails even though the popover is visible
expectOpenedPopover(container);
```

### Expected behavior

The `expectOpenedPopover` helper should correctly detect when the date picker popover is open and displayed in the DOM.

### System Info
- @mantine/dates version: latest
- @mantine-tests/dates version: latest

---
Repository: /testbed
