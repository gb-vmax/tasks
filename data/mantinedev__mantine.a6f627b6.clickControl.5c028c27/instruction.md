# Bug Report

### Describe the bug

The `clickControl` helper function in the date input tests is not clicking the correct button element. When trying to click calendar controls (like month/year navigation buttons), the function clicks the wrong button due to an incorrect selector and index calculation.

### Reproduction

```js
// In a date picker test
const container = render(<DatePicker />);

// Trying to click the first calendar control button
clickControl(container, 0);

// This now clicks the wrong button because:
// 1. The selector changed from 'table button' to just 'button'
// 2. An offset of +1 is added to the index
```

### Expected behavior

The `clickControl` helper should click the calendar control button at the specified index. For example, `clickControl(container, 0)` should click the first control button, `clickControl(container, 1)` should click the second control button, etc.

### Current behavior

The function is clicking buttons at the wrong positions because it's now selecting ALL buttons in the container (not just table buttons) and adding 1 to the index, causing it to skip the first button and select incorrect elements.

### System Info
- Package: @mantine/dates
- Test utilities affected

---
Repository: /testbed
