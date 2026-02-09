# Bug Report

### Describe the bug

I'm experiencing an issue with the date picker controls when trying to interact with calendar buttons. When clicking on calendar controls using the helper function, it seems to be selecting the wrong button element.

### Reproduction

```tsx
// When trying to click a specific calendar control
const container = render(<DatePicker />).container;

// Attempting to click the second calendar button
clickControl(container, 1);

// Expected: Should click the second button in the calendar
// Actual: Throws an error - cannot read querySelector of undefined
```

The issue appears when there are multiple calendar tables rendered and you're trying to access buttons beyond the first table. The selector seems to be looking for buttons in the wrong scope.

### Expected behavior

The `clickControl` helper should correctly select and click the button at the specified index across all calendar tables, not try to access a table at that index.

### System Info
- Mantine version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
