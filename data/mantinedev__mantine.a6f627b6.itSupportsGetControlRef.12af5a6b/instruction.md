# Bug Report

### Describe the bug

The `__getControlRef` callback is being called with incorrect arguments. It seems like one of the expected parameters is missing when the callback is invoked.

### Reproduction

```tsx
import { DatePicker } from '@mantine/dates';

const ref = (rowIndex, cellIndex, element) => {
  console.log('Row:', rowIndex);
  console.log('Cell:', cellIndex);
  console.log('Element:', element);
};

<DatePicker __getControlRef={ref} />
```

When the callback is triggered, it only receives 2 arguments instead of the expected 3 (rowIndex, cellIndex, and the HTML element).

### Expected behavior

The `__getControlRef` callback should be called with three arguments:
1. Row index (number)
2. Cell index (number)  
3. HTML button element

Currently it appears to only be passing 2 arguments.

### System Info
- @mantine/dates: latest
- React: 18.x

---
Repository: /testbed
