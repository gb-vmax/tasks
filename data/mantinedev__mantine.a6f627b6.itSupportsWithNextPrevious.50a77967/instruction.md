# Bug Report

### Describe the bug

I'm experiencing an issue with the `withNext` and `withPrevious` props on date picker components. When I set `withNext={false}`, the previous button disappears instead of the next button. Similarly, when I set `withPrevious={true}`, the next button appears instead of the previous button.

### Reproduction

```jsx
// Setting withNext to false should hide the next button, but hides previous instead
<DatePicker withNext={false} />
// Expected: next button hidden
// Actual: previous button hidden

// Setting withPrevious to true should show the previous button, but shows next instead
<DatePicker withPrevious={true} />
// Expected: previous button shown
// Actual: next button shown
```

### Expected behavior

- `withNext={false}` should hide the "next" navigation button
- `withPrevious={false}` should hide the "previous" navigation button
- `withNext={true}` should show the "next" navigation button
- `withPrevious={true}` should show the "previous" navigation button

The props seem to be controlling the wrong buttons - they appear to be swapped.

### System Info
- @mantine/dates: latest
- React: 18.x

---
Repository: /testbed
