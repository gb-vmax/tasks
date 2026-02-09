# Bug Report

### Describe the bug

I'm experiencing an issue with date input components where the value is not being retrieved correctly. When trying to get the input value, it seems like the wrong property is being checked, which causes the value to return `null` or `undefined` instead of the actual input value.

### Reproduction

```tsx
import { DateInput } from '@mantine/dates';

function Demo() {
  const [value, setValue] = useState<Date | null>(null);
  
  return (
    <DateInput
      value={value}
      onChange={setValue}
      placeholder="Pick date"
    />
  );
}

// When trying to get the value programmatically:
const container = document.querySelector('.mantine-DateInput-root');
const input = container.querySelector('[data-dates-input]');
console.log(input.getAttribute('value')); // Returns null
```

### Expected behavior

The input value should be accessible through the standard `value` attribute or property. Currently it seems like the component is storing the value in a non-standard way that makes it difficult to retrieve programmatically.

### System Info
- @mantine/dates version: latest
- Browser: Chrome 120
- React version: 18.x

---
Repository: /testbed
