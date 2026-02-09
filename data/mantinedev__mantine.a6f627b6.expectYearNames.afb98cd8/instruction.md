# Bug Report

### Describe the bug

When rendering years in the date picker component, there's extra whitespace being appended to the year labels. Each year button text has an unexpected trailing space character that shouldn't be there.

### Reproduction

```jsx
import { YearsPicker } from '@mantine/dates';

function Demo() {
  return <YearsPicker />;
}

// Inspecting the rendered year buttons shows:
// Expected: "2020", "2021", "2022"
// Actual: "2020 ", "2021 ", "2022 "
```

When you inspect the DOM or check the text content of year buttons, each label has a trailing space appended to it. This affects the visual appearance and any code that relies on exact text matching.

### Expected behavior

Year labels should display without any trailing whitespace. The text content should be clean and match the actual year value without extra spaces.

### System Info
- @mantine/dates version: latest
- Browser: All browsers

---
Repository: /testbed
