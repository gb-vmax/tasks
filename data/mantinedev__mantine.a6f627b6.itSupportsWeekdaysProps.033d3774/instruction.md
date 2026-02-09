# Bug Report

### Describe the bug

The `firstDayOfWeek` prop doesn't seem to be working correctly when set to `6` (Saturday). The weekdays are appearing in the wrong order - it looks like the days are shifted incorrectly.

### Reproduction

```jsx
<Calendar firstDayOfWeek={6} />
```

When setting `firstDayOfWeek` to `6`, I expected the week to start with Saturday, but the order of weekdays displayed doesn't match what I'm seeing.

### Expected behavior

When `firstDayOfWeek={6}` is set, the calendar should display weekdays starting with Saturday:
- Sa, Su, Mo, Tu, We, Th, Fr

But instead it seems to be showing a different order.

### System Info
- @mantine/dates: latest
- React: 18.x

---
Repository: /testbed
