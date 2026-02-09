# Bug Report

### Describe the bug

When using keyboard navigation in date picker components, pressing the Enter key on a calendar cell is not triggering the `onControlKeydown` callback with the correct cell information. The callback is being invoked with incorrect `cellIndex` values.

### Reproduction

```jsx
import { Calendar } from '@mantine/dates';

function Demo() {
  const handleKeyDown = (payload) => {
    console.log('Key pressed on cell:', payload);
    // Expected: { rowIndex: 0, cellIndex: 0, date: '...' }
    // Actual: { rowIndex: 0, cellIndex: 1, date: '...' }
  };

  return (
    <Calendar onControlKeydown={handleKeyDown} />
  );
}
```

Steps to reproduce:
1. Render a Calendar component with `onControlKeydown` prop
2. Focus on the first cell in the calendar table
3. Press the Enter key
4. Check the payload received in the callback

The `cellIndex` in the payload is off by one - it returns `1` instead of `0` for the first cell.

### Expected behavior

When pressing Enter on the first calendar cell (index 0), the `onControlKeydown` callback should receive:
```js
{ rowIndex: 0, cellIndex: 0, date: '...' }
```

Instead, it's currently receiving:
```js
{ rowIndex: 0, cellIndex: 1, date: '...' }
```

This makes it difficult to correctly handle keyboard interactions with specific date cells.

### System Info
- @mantine/dates: latest
- @mantine/core: latest

---
Repository: /testbed
