# Bug Report

### Describe the bug

The HiddenDatesInput component is displaying incorrect output when working with date ranges. When only a start date is provided (without an end date), the component shows nothing instead of showing the start date with a dash. Similarly, when only an end date is provided, it's not displaying correctly.

### Reproduction

```jsx
// Case 1: Only start date provided
<HiddenDatesInput 
  type="range"
  value={[new Date('2024-01-15'), null]}
/>
// Expected: "2024-01-15 –"
// Actual: "" (empty string)

// Case 2: Only end date provided  
<HiddenDatesInput
  type="range"
  value={[null, new Date('2024-01-20')]}
/>
// Expected: "– 2024-01-20"
// Actual: "2024-01-20 –" (shows start date format instead)
```

Also noticed that when using `type="multiple"` with an array of dates, the output seems to be broken - getting a weird result that doesn't look like the expected comma-separated date list.

### Expected behavior

- When start date exists but end date is null: should display `"startDate –"`
- When end date exists but start date is null: should display `"– endDate"`
- For multiple dates: should display as comma-separated string like `"date1, date2, date3"`

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
