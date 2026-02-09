# Bug Report

### Describe the bug

When clearing a selected date in a date input component, the placeholder text is not being displayed correctly. After clicking to deselect/clear a date, the input field remains empty instead of showing the configured placeholder text.

### Reproduction

```jsx
const [value, setValue] = useState(new Date());

<DateInput
  value={value}
  onChange={setValue}
  placeholder="test-placeholder"
  clearable
/>
```

Steps to reproduce:
1. Set up a date input with a placeholder and an initial value
2. Click to open the date picker
3. Click to clear/deselect the current date
4. The input field should display the placeholder text but it doesn't

### Expected behavior

After clearing the selected date, the input field should display the placeholder text ("test-placeholder" in this example). The component should properly show placeholder text when no date is selected.

### Additional context

This seems to affect the behavior when interacting with the date controls. The onChange callback is also receiving unexpected values (including `null`) when dates are being selected/cleared.

---
Repository: /testbed
