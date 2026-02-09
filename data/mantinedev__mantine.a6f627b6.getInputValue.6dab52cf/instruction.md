# Bug Report

### Describe the bug

I'm experiencing an issue with date input components where the value retrieval is not working correctly. When trying to get the current value from a date input field, it returns `null` or undefined instead of the actual input value.

### Reproduction

```js
import { DateInput } from '@mantine/dates';

function MyComponent() {
  const [value, setValue] = useState(new Date());
  
  return <DateInput value={value} onChange={setValue} />;
}

// When trying to get the input value programmatically:
const container = screen.getByRole('textbox').closest('[data-dates-input]');
const currentValue = container.querySelector('input')?.value;
// Returns null instead of the formatted date string
```

### Expected behavior

The date input value should be retrievable and return the formatted date string that's currently displayed in the input field.

### System Info

- @mantine/dates version: latest
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
