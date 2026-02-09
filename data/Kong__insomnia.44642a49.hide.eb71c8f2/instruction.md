# Bug Report

### Describe the bug
The timestamp template tag's custom format field is not showing up when selecting "custom" as the date format type. The field remains hidden regardless of the format selection.

### Reproduction
```js
// In the templating system
1. Add a timestamp template tag
2. Select "custom" from the format dropdown
3. The custom format template input field doesn't appear

// The hide function should show the field when format is 'custom'
// but it's currently always hiding it
```

### Expected behavior
When selecting "custom" as the date format type, the "Custom Format Template" input field should become visible to allow users to enter their custom date format string (e.g., 'MMMM Do YYYY, h:mm:ss a').

### Additional context
This seems to have broken recently. The custom format option is still in the dropdown but the corresponding input field never appears, making it impossible to actually use custom date formatting.

---
Repository: /testbed
