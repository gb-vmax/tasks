# Bug Report

### Describe the bug

When using date components with weekday headers, the first column header is being included in the weekday names, causing incorrect weekday display. It appears that an extra column header element is being rendered before the actual weekday names.

### Reproduction

```jsx
import { Calendar } from '@mantine/dates';

function Demo() {
  return (
    <Calendar />
  );
}
```

When inspecting the rendered weekday headers, there's an unexpected additional column header element at the beginning that shouldn't be part of the weekday names array.

### Expected behavior

The weekday names should only include the 7 days of the week (e.g., Mon, Tue, Wed, Thu, Fri, Sat, Sun) without any extra column headers prepended to the list.

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
