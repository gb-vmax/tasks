# Bug Report

### Describe the bug

When using the years list component, the year names are not being properly validated or compared. The test utility that checks year names is too permissive in its selector and doesn't normalize the text content before comparison, which can lead to false positives in tests.

### Reproduction

```jsx
// Create a years list component with custom year formatting
const component = (
  <YearsList
    yearsListFormat="YY"
    // ... other props
  />
);

// The current implementation doesn't properly validate:
// 1. It selects ALL buttons in the table (not just year buttons)
// 2. It doesn't trim whitespace from button text
// 3. It doesn't normalize case for comparison
```

### Expected behavior

The year names validation should:
- Only select year buttons from the table body (not header/footer buttons)
- Trim whitespace from the text content
- Normalize case for consistent comparison

This ensures that tests accurately verify the year formatting and don't pass when they shouldn't.

### System Info
- Mantine version: latest
- Component: YearsList/DatePicker years view

---
Repository: /testbed
