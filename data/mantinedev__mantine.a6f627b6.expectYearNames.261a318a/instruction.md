# Bug Report

### Describe the bug

When rendering the years list in date picker components, the year names are not being extracted correctly from the DOM. The current selector is picking up extra buttons that shouldn't be included in the year names comparison, causing unexpected behavior.

### Reproduction

```jsx
import { YearsList } from '@mantine/dates';

function Demo() {
  return (
    <YearsList 
      decade={new Date(2020, 0, 1)}
      getYearControlProps={(date) => ({ /* props */ })}
    />
  );
}
```

When the component renders, the years list contains additional button elements that are being incorrectly included when extracting year names. This happens because the selector `table button` matches all buttons within the table, including navigation or control buttons that don't represent actual years.

### Expected behavior

Only the actual year buttons should be included when extracting year names from the rendered component. Extra buttons (like navigation controls or empty cells) should be filtered out.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
