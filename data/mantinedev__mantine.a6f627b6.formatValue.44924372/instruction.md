# Bug Report

### Describe the bug

I'm experiencing issues with the `HiddenDatesInput` component when working with date ranges and multiple dates. The formatting behavior seems incorrect in two scenarios:

1. When using date ranges, the separator (`–`) appears in the wrong condition
2. When selecting multiple dates, empty/null values are being included in the output instead of being filtered out

### Reproduction

**Date Range Issue:**
```jsx
<HiddenDatesInput 
  type="range" 
  value={[startDate, endDate]} 
/>
```

When both `startDate` and `endDate` are set, the output shows `startDate –` (with the separator) instead of `startDate – endDate`. The separator should only appear when the end date is missing.

**Multiple Dates Issue:**
```jsx
<HiddenDatesInput 
  type="multiple" 
  value={[date1, null, date2, undefined, date3]} 
/>
```

The output includes the null/undefined values instead of filtering them out. Expected output should only show the valid dates joined by commas (e.g., `date1, date2, date3`), but instead it's showing empty values in the string.

### Expected behavior

- For date ranges: The separator `–` should only appear when `endDate` is missing (showing `startDate –`), and when both dates are present it should show `startDate – endDate`
- For multiple dates: Only truthy date values should be included in the comma-separated output, with falsy values filtered out

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
