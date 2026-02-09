# Bug Report

### Describe the bug

When rendering a months list component, the month names are not being extracted correctly from the DOM. The selector used to find month buttons appears to be targeting the wrong elements, causing month name validation to fail.

### Reproduction

```jsx
import { MonthsList } from '@mantine/dates';

function Demo() {
  return (
    <MonthsList 
      date={new Date(2024, 0)}
      locale="en"
    />
  );
}
```

When trying to verify the rendered month names, the component structure doesn't match the expected query selector. The months are rendered in a different container structure than what's being queried.

### Expected behavior

The component should render month buttons in a way that allows them to be properly selected and their text content to be extracted. Month names should be accessible via a consistent selector pattern.

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
