# Bug Report

### Describe the bug
The `__onDayClick` callback is being triggered even when clicking outside of day cells in the calendar component. It appears that clicks on the container element itself are now invoking the callback, when it should only be called when clicking on actual day buttons.

### Reproduction
```jsx
const [clicked, setClicked] = useState(null);

<DatePicker
  __onDayClick={(event, date) => {
    console.log('Clicked:', date);
    setClicked(date);
  }}
/>
```

Steps to reproduce:
1. Render a date picker component with an `__onDayClick` handler
2. Click anywhere on the calendar container (not on a specific day button)
3. The callback gets triggered even though no day was actually clicked

### Expected behavior
The `__onDayClick` callback should only fire when clicking on actual day cells/buttons within the calendar, not when clicking on the container or other non-day elements.

### System Info
- Mantine version: latest
- React version: 18.x

---
Repository: /testbed
