# Bug Report

### Describe the bug

The `withNext={false}` prop is not working correctly - the next button still appears in the DOM even when explicitly set to false. Additionally, when using `withPrevious` prop, it seems to be checking for the wrong button element.

### Reproduction

```jsx
import { YourDateComponent } from '@mantine/dates';

// Case 1: withNext={false} should hide the next button
<YourDateComponent withNext={false} />
// Expected: No next button in DOM
// Actual: Next button is still present

// Case 2: withPrevious prop seems to check wrong element
<YourDateComponent withPrevious />
// Expected: Previous button should be validated
// Actual: Appears to be checking for next button instead
```

### Expected behavior

1. When `withNext={false}` is set, the next button should not be rendered in the DOM
2. When `withPrevious` is set, the component should correctly validate the presence of the previous button (not the next button)

### System Info
- @mantine/dates: latest
- React: 18.x

---
Repository: /testbed
