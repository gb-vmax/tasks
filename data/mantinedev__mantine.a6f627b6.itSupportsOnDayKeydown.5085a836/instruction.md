# Bug Report

### Describe the bug

The `__onDayKeydown` handler is not being triggered when pressing the space key on a calendar day button. It appears that keyboard navigation for selecting dates is broken.

### Reproduction

```tsx
const spy = jest.fn();

<Component
  __onDayKeydown={spy}
  date={new Date(2022, 3, 11)}
/>

// Try to select a day using keyboard
const dayButton = container.querySelector('table button');
await userEvent.type(dayButton, '{space}');

// Expected: spy should be called with day information
// Actual: spy is not called
```

### Expected behavior

When a user presses the space key on a focused calendar day button, the `__onDayKeydown` callback should be triggered with the correct day information including `rowIndex`, `cellIndex`, and `date`.

This is important for keyboard accessibility - users should be able to navigate and select dates using only the keyboard.

### System Info
- Mantine version: latest
- React version: 18.x

---
Repository: /testbed
