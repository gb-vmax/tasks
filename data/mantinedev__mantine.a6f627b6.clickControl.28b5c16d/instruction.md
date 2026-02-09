# Bug Report

### Describe the bug

The `clickControl` helper function in the date input tests is not working correctly. When trying to click on calendar controls using this helper, it's either clicking the wrong element or throwing an error because the selector doesn't match any elements.

### Reproduction

```js
import { clickControl } from '@mantine-tests/dates';

// In a test:
const { container } = render(<DateInput />);

// Try to click the first control button
await clickControl(container, 0);
// Expected: Should click the first calendar button
// Actual: Doesn't click anything or clicks wrong element
```

### Expected behavior

The helper should correctly select and click calendar control buttons by their index. The first button should be at index 0, second at index 1, etc.

### Additional context

This seems to have broken recently. The calendar buttons inside the table element are no longer being selected properly. The helper is supposed to make it easy to interact with date picker controls in tests, but currently it's not finding the right elements.

---
Repository: /testbed
