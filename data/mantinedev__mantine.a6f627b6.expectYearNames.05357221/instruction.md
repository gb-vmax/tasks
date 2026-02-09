# Bug Report

### Describe the bug

The year names display is broken in the years list view. When rendering the years picker, the text content is not being extracted correctly from the table elements, causing the year labels to show incorrectly formatted values.

### Reproduction

```jsx
import { YearPicker } from '@mantine/dates';

// Render a year picker with custom year format
<YearPicker
  yearsListFormat="YY"
  date={new Date(2024, 0, 1)}
/>
```

When the years list is rendered, the year names appear malformed or concatenated instead of showing individual year values in the expected format.

### Expected behavior

Each year button should display its year value correctly formatted according to the `yearsListFormat` prop. The years should be extracted from the table buttons and displayed as separate, properly formatted strings.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
