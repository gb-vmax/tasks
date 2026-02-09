# Bug Report

### Describe the bug

The navigation controls in the date picker header are triggering callbacks multiple times when they should only fire once. When clicking the "previous" button, the `onNext` callback is being invoked instead of `onPrevious`, and both callbacks are being called more times than expected.

### Reproduction

```jsx
const [value, setValue] = useState(new Date());

<DatePicker
  value={value}
  onChange={setValue}
  onNext={() => console.log('Next clicked')}
  onPrevious={() => console.log('Previous clicked')}
/>
```

When clicking the previous button:
- Expected: "Previous clicked" logged once
- Actual: "Next clicked" logged twice, "Previous clicked" not logged at all

Similarly, when clicking the level control button, the `onLevelClick` callback fires twice instead of once.

### Expected behavior

- Clicking the "next" button should call `onNext` exactly once
- Clicking the "previous" button should call `onPrevious` exactly once  
- Clicking the level control should call `onLevelClick` exactly once
- Each callback should only be invoked for its corresponding button click

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
