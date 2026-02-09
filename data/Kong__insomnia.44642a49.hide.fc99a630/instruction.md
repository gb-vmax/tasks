# Bug Report

### Describe the bug

When using the `parameter` attribute in template tags, an extra unnecessary input field is being displayed in the UI. This field should be hidden when the parameter index is specified numerically (when `args[2]` is a number), but it's currently showing up.

### Reproduction

1. Create a template tag with the `parameter` attribute
2. Set the attribute value to `'parameter'`
3. Provide a numeric value as the third argument (parameter index)
4. Observe that an extra input field appears in the template editor

Expected: The field should be hidden when a numeric parameter index is provided, similar to how fields are hidden for 'url', 'oauth2', etc.

Actual: The field is displayed even though it shouldn't be visible in this case.

### Additional context

This seems to affect the template tag UI specifically when working with parameter-based attributes. Other attributes like 'url', 'oauth2', 'name', and 'folder' correctly hide their fields as expected.

---
Repository: /testbed
