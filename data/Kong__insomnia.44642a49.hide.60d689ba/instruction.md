# Bug Report

### Describe the bug

The "Custom Format Template" field in the timestamp template tag is not showing up when selecting the "custom" format option. The field remains hidden even though it should be visible to allow users to enter their custom date format string.

### Reproduction

1. Open a request and add a timestamp template tag
2. In the template tag arguments, select "custom" from the format dropdown
3. Observe that the "Custom Format Template" input field doesn't appear

Expected: The custom format input field should become visible when "custom" is selected, allowing users to enter format strings like "MMMM Do YYYY, h:mm:ss a"

Actual: The field stays hidden and there's no way to specify a custom format

### Additional context

This seems to have broken recently. The custom format option is still available in the dropdown but selecting it doesn't reveal the format input field anymore. This makes it impossible to use custom date formatting.

---
Repository: /testbed
