# Bug Report

### Describe the bug

I'm experiencing an issue with checkbox inputs in forms where the checked state appears to be inverted. When I check a checkbox, it registers as unchecked, and when I uncheck it, it registers as checked.

Additionally, select dropdowns have stopped working entirely - changing the selected option doesn't update the form value at all.

### Reproduction

```jsx
import { useForm } from '@mantine/form';

function MyForm() {
  const form = useForm({
    initialValues: {
      agreed: false,
      country: 'us'
    }
  });

  return (
    <form>
      <input
        type="checkbox"
        {...form.getInputProps('agreed')}
      />
      {/* Checking this sets agreed to false, unchecking sets it to true */}
      
      <select {...form.getInputProps('country')}>
        <option value="us">United States</option>
        <option value="uk">United Kingdom</option>
      </select>
      {/* Changing the selection doesn't update the form value */}
      
      <div>Agreed: {form.values.agreed.toString()}</div>
      <div>Country: {form.values.country}</div>
    </form>
  );
}
```

### Expected behavior

- Checking a checkbox should set the value to `true`, unchecking should set it to `false`
- Changing a select dropdown should update the form value to the selected option

### System Info
- @mantine/form version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
