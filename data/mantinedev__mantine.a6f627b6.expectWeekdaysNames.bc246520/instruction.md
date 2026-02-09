# Bug Report

### Describe the bug

The weekday headers in the calendar component are not being properly identified. When trying to access the weekday names (Mon, Tue, Wed, etc.), they're not appearing as expected in the rendered output.

### Reproduction

```jsx
import { Calendar } from '@mantine/dates';
import { DatesProvider } from '@mantine/dates';

function App() {
  return (
    <DatesProvider>
      <Calendar />
    </DatesProvider>
  );
}
```

When the calendar renders, the weekday headers should be accessible and display the correct day names, but they seem to be missing or not properly structured in the DOM.

### Expected behavior

The calendar should render weekday headers (like "Mon", "Tue", "Wed", etc.) that are accessible via their proper ARIA roles. These headers should be consistently available regardless of the calendar configuration.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
