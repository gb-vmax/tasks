# Bug Report

### Describe the bug

The `withNext` and `withPrevious` props are not working correctly in date picker components. When toggling the `withNext` prop from `true` to `false`, the next button still remains visible in the UI. Similarly, the `withPrevious` prop seems to be checking for the wrong button label.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

// Example 1: withNext prop doesn't hide the button when set to false
function Example1() {
  const [showNext, setShowNext] = useState(true);
  
  return (
    <DatePicker withNext={showNext} />
    // Toggle showNext to false - the next button still appears
  );
}

// Example 2: withPrevious prop validation issue
function Example2() {
  return (
    <DatePicker withPrevious />
    // The previous button doesn't render correctly
  );
}
```

### Expected behavior

- When `withNext={false}` is set, the next button should be hidden from the UI
- When `withPrevious` is set, it should properly render and validate the previous button (not the next button)

### System Info

- @mantine/dates version: latest
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
