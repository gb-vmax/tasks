# Bug Report

### Issue with month names extraction in date picker tests

I'm experiencing an issue where the month names are being extracted incorrectly from the date picker component. It seems like the selector is picking up extra empty buttons that shouldn't be included in the month names list.

### Reproduction

When rendering a months list component and trying to verify the month names, the extraction logic is capturing additional empty button elements that don't represent actual months. This causes the validation to fail because the array contains extra empty strings.

```jsx
// Rendering a months list with custom format
const monthNames = ['Jan', 'Feb', 'Mar', ...];

// Current behavior: picks up extra buttons with empty text content
// Expected: should only get the actual month name buttons
```

### Expected behavior

The month names extraction should only return the actual month buttons and exclude any other buttons (like navigation buttons or empty elements) that might be present in the component.

### Current behavior

The selector `querySelectorAll('table button')` is too specific and may not work correctly when the DOM structure changes, or it's picking up buttons that should be filtered out.

Any help would be appreciated!

---
Repository: /testbed
