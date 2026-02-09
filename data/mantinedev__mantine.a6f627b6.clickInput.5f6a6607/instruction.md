# Bug Report

### Describe the bug

I'm experiencing an issue with date input components where clicking on the input field doesn't seem to work as expected. It appears that when there are multiple date inputs on the page, the click interaction is targeting the wrong element.

### Reproduction

```jsx
import { DateInput } from '@mantine/dates';

function MyComponent() {
  return (
    <div>
      <DateInput label="First date" />
      <DateInput label="Second date" />
    </div>
  );
}
```

When trying to interact with the first date input (clicking to open the calendar popover), nothing happens. The click seems to be going to a different input element instead of the one I'm actually clicking on.

### Expected behavior

Clicking on a date input should open its associated calendar popover and allow date selection for that specific input field. Each date input should respond independently to user interactions.

### System Info
- @mantine/dates version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
