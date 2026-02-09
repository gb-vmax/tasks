# Bug Report

### Describe the bug

When using string values directly in Combobox data, the label is no longer being displayed correctly. The dropdown shows empty labels even though the values are properly set as strings.

### Reproduction

```jsx
import { Combobox } from '@mantine/core';

const data = ['Apple', 'Banana', 'Orange'];

<Combobox data={data} />
```

When rendering this component, the dropdown options appear but without any visible text labels. The values are still there (can be selected), but nothing is displayed to the user.

### Expected behavior

When passing an array of strings to the Combobox component, each string should be used as both the value and the label. The dropdown should display the text "Apple", "Banana", "Orange" as visible options.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
