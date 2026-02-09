# Bug Report

### Describe the bug

I'm experiencing an issue with the date picker header controls where clicking the previous button or the level button seems to trigger the callback handlers twice instead of once. This appears to be causing duplicate event handling in my application.

### Reproduction

```jsx
const [date, setDate] = useState(new Date());
const handleNext = () => {
  console.log('Next clicked');
  // This logs twice when clicking previous button
};

const handlePrevious = () => {
  console.log('Previous clicked');
};

<DatePicker
  value={date}
  onChange={setDate}
  onNext={handleNext}
  onPrevious={handlePrevious}
/>
```

When I click the previous arrow button, I notice that `handleNext` is being called instead of (or in addition to?) `handlePrevious`. Similar behavior happens with the level button where the callback fires multiple times.

### Expected behavior

- Clicking the "previous" button should only call `onPrevious` once
- Clicking the "next" button should only call `onNext` once  
- Level button clicks should trigger their handler exactly once

Currently it seems like the wrong handlers are being invoked or they're being called multiple times per click.

### System Info

- @mantine/dates: latest
- React: 18.x

---
Repository: /testbed
