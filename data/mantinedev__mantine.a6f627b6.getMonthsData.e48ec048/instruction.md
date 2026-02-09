# Bug Report

### Describe the bug

The months grid is displaying incorrectly with a 5x2 layout instead of the expected 4x3 layout. When rendering the MonthsList component, I'm seeing 5 rows with only 2 months each, which looks really weird and breaks the UI.

### Reproduction

```js
import { MonthsList } from '@mantine/dates';

// Render MonthsList for any year
<MonthsList year="2024" />
```

The component renders a grid with 5 rows and 2 columns instead of the standard 4 rows and 3 columns calendar layout.

### Expected behavior

The months should be displayed in a 4x3 grid (4 rows, 3 columns per row), showing all 12 months of the year in a properly formatted calendar layout like:

```
Jan  Feb  Mar
Apr  May  Jun
Jul  Aug  Sep
Oct  Nov  Dec
```

Instead, it's currently showing a 5x2 layout which doesn't make sense for displaying 12 months.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
