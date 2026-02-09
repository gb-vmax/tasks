# Bug Report

### Describe the bug

When using `getInputProps()` with `withFocus: true`, the field is being marked as touched immediately when the form is rendered, before any user interaction. The field should only be marked as touched when the user actually focuses on the input, not on initial render.

### Reproduction

```jsx
import { useForm } from '@mantine/form';

function MyForm() {
  const form = useForm({
    initialValues: {
      email: '',
    },
  });

  return (
    <form>
      <input {...form.getInputProps('email', { withFocus: true })} />
      {/* Field shows as touched even before user interacts with it */}
      <div>Touched: {form.isTouched('email') ? 'Yes' : 'No'}</div>
    </form>
  );
}
```

### Expected behavior

The field should show as "not touched" initially. It should only be marked as touched when the user focuses on the input field. Currently, it's marked as touched immediately on render.

### System Info

- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
