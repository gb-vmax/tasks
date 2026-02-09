# Bug Report

### Describe the bug

When using the YearsList component with multiple selected years, keyboard navigation focuses on the wrong year. Instead of focusing on the first selected year in the list, it seems to be focusing on the last one, which makes navigation feel backwards and unintuitive.

### Reproduction

```jsx
import { YearsList } from '@mantine/dates';

// Setup with multiple years where some are selected
const years = [2020, 2021, 2022, 2023, 2024];
const selectedYears = [2021, 2023]; // Multiple selected years

<YearsList
  decade={new Date(2020, 0)}
  getYearControlProps={(year) => ({
    selected: selectedYears.includes(year)
  })}
/>
```

When tabbing into the component, focus goes to 2023 (the last selected year) instead of 2021 (the first selected year). Similarly, when no years are selected, focus seems to go to the last enabled year in the list rather than the first one.

### Expected behavior

- When multiple years are selected, tab order should focus on the **first** selected year
- When no years are selected, tab order should focus on the **first** enabled year in the list
- This provides a more natural top-to-bottom navigation experience

### System Info
- @mantine/dates version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
