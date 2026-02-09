# Bug Report

### Describe the bug

When rendering calendar components, the weekday header names are being duplicated in the DOM. Each weekday appears twice as a column header, but only the first occurrence should be present. This is causing issues with accessibility and DOM structure validation.

### Reproduction

```jsx
import { Calendar } from '@mantine/dates';

function App() {
  return <Calendar />;
}
```

When inspecting the rendered output, each weekday header (Mon, Tue, Wed, etc.) appears twice in the column headers. For example, if you query all elements with role `columnheader`, you'll get duplicate entries like:

```
['Mon', 'Mon', 'Tue', 'Tue', 'Wed', 'Wed', 'Thu', 'Thu', 'Fri', 'Fri', 'Sat', 'Sat', 'Sun', 'Sun']
```

### Expected behavior

Each weekday should only appear once as a column header:

```
['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
```

### System Info

- @mantine/dates version: latest
- @mantine/core version: latest
- React version: 18.x

This seems to be affecting all date picker components that render weekday headers. The duplication is causing problems with screen readers and automated accessibility testing tools.

---
Repository: /testbed
