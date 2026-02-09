# Bug Report

### Describe the bug

The `__getControlRef` callback is not being called the expected number of times for date picker controls. When rendering a date picker component, the callback that receives control references appears to be called one fewer time than the actual number of controls present.

### Reproduction

```tsx
import { useRef } from 'react';

const refCallback = (levelIndex: number, rowIndex: number, node: HTMLButtonElement) => {
  console.log('Control ref received:', levelIndex, rowIndex, node);
};

// Render a date picker with multiple controls
<DatePicker __getControlRef={refCallback} />

// Expected: callback called N times (once per control)
// Actual: callback called N-1 times (missing one control)
```

### Expected behavior

The `__getControlRef` callback should be invoked once for each control element in the date picker, allowing all control refs to be captured properly. If there are 7 controls, the callback should be called 7 times.

### Additional context

This seems to affect the ability to programmatically access all control elements in the date picker. The last control's reference is not being passed to the callback function.

---
Repository: /testbed
