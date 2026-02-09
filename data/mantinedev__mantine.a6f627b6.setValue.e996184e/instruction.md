# Bug Report

### Describe the bug

I'm experiencing an issue with form inputs where checkbox values are being set incorrectly. When I click on a checkbox, it's setting the text value instead of the checked state (true/false).

### Reproduction

```jsx
import { useForm } from '@mantine/form';

function MyForm() {
  const form = useForm({
    initialValues: {
      acceptTerms: false,
    },
  });

  return (
    <form>
      <input
        type="checkbox"
        {...form.getInputProps('acceptTerms')}
      />
    </form>
  );
}
```

When I click the checkbox:
- Expected: `form.values.acceptTerms` should be `true` or `false`
- Actual: `form.values.acceptTerms` is set to `"on"` (the checkbox's value attribute)

### Additional context

This is causing validation issues in my forms since the field is expecting a boolean but receiving a string. Also noticed that text inputs and textareas seem to have issues when the value is empty - they're not updating at all in that case.

The behavior was working correctly before, not sure what changed.

---
Repository: /testbed
