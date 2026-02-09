# Bug Report

### Describe the bug

The date picker popover is not being detected correctly when it opens. After clicking on a date input field, the popover appears visually on screen but the test helper function `expectOpenedPopover` fails to confirm its presence.

### Reproduction

```tsx
import { render } from '@testing-library/react';
import { DateInput } from '@mantine/dates';
import { clickInput, expectOpenedPopover } from '@mantine-tests/dates';

const { container } = render(<DateInput />);
clickInput(container);

// Popover is visible on screen but this check fails
expectOpenedPopover(container);
```

### Expected behavior

When the date input is clicked and the popover opens, `expectOpenedPopover` should successfully verify that the dropdown with `data-dates-dropdown` attribute is present in the DOM.

### System Info
- @mantine/dates version: latest
- Testing library: @testing-library/react

---
Repository: /testbed
