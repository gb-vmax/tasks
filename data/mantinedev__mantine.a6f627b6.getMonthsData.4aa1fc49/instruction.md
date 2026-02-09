# Bug Report

### Describe the bug

The `MonthsList` component is displaying incorrect months for the year. All months appear to be shifted by one month forward - for example, February is shown where January should be, March where February should be, etc.

### Reproduction

```js
import { getMonthsData } from '@mantine/dates';

const monthsData = getMonthsData('2024');
console.log(monthsData[0][0]); // Expected: '2024-01-01' (January)
                                 // Actual: '2024-02-01' (February)
```

When rendering a MonthsList component for any year, the first month displayed is February instead of January, and the pattern continues with all subsequent months being off by one.

### Expected behavior

The months should start from January (month 01) and proceed in order through December (month 12). The first element in the returned array should represent January of the given year.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
