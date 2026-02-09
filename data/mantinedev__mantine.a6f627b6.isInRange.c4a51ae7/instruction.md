# Bug Report

### Date range boundary check not working correctly

I'm experiencing an issue with date range validation where dates at the exact boundaries of a range are not being handled properly. The `isInRange` function seems to be incorrectly including/excluding dates that fall on the start or end dates of the range.

### Reproduction
```js
const range = ['2024-01-01', '2024-01-31'];

// These should return true but behave unexpectedly
isInRange('2024-01-01', range); // Start date
isInRange('2024-01-31', range); // End date

// Dates clearly within the range
isInRange('2024-01-15', range); // Middle date
```

### Expected behavior
- Dates that fall exactly on the start date should be included in the range
- Dates that fall exactly on the end date should be included in the range  
- Dates between the start and end should be included
- Dates outside the range should be excluded

### Additional context
This is affecting date pickers where users select a date range and then try to select dates within that range. The boundary dates are behaving inconsistently.

Using @mantine/dates latest version.

---
Repository: /testbed
