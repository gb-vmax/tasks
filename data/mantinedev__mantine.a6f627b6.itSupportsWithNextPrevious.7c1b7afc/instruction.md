# Bug Report

### Describe the bug

The `withPrevious` prop doesn't seem to be working correctly in date picker components. When I set `withPrevious={true}`, the previous navigation button doesn't appear, but the next button shows up instead.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

function App() {
  return (
    <DatePicker withPrevious />
  );
}
```

When rendering this component:
1. I expect to see a "prev" button (previous navigation)
2. Instead, only the "next" button appears
3. The "prev" button is completely missing

### Expected behavior

When `withPrevious={true}` is set, the component should display a previous navigation button with the aria-label "prev". The next button should only appear when `withNext` is explicitly set.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
