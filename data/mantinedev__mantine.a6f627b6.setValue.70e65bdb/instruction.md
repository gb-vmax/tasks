# Bug Report

### Describe the bug

I'm experiencing an issue with form inputs where disabled checkboxes are still triggering value changes. When a checkbox is disabled, clicking on it shouldn't update the form state, but currently it does.

Additionally, I noticed that empty values from textarea and select elements are not being set properly - they seem to be ignored instead of updating the field to an empty string.

### Reproduction

```jsx
// Disabled checkbox still updates form value
const form = useForm({
  initialValues: {
    terms: false
  }
});

<Checkbox 
  {...form.getInputProps('terms')}
  disabled
/>
// Clicking the disabled checkbox changes form.values.terms

// Empty textarea value is ignored
const form = useForm({
  initialValues: {
    description: 'initial text'
  }
});

<Textarea {...form.getInputProps('description')} />
// Clearing the textarea doesn't update form.values.description to empty string
```

### Expected behavior

1. Disabled checkboxes should not trigger onChange handlers or update form values
2. Clearing a textarea or select should properly set the value to an empty string in the form state

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
