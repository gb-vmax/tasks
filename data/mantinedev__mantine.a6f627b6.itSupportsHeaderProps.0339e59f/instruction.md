# Bug Report

### Describe the bug

The `nextLabel` and `previousLabel` props appear to be swapped in date picker components. When setting a custom label for the "next" button, it gets applied to the "previous" button instead, and vice versa.

### Reproduction

```tsx
<DatePicker
  nextLabel="test-next-label"
  previousLabel="test-previous-label"
/>
```

When inspecting the rendered buttons:
- The button with `data-direction="next"` has `aria-label="test-previous-label"` (should be "test-next-label")
- The button with `data-direction="previous"` has `aria-label="test-next-label"` (should be "test-previous-label")

### Expected behavior

The `nextLabel` prop should set the aria-label for the next button (`data-direction="next"`), and the `previousLabel` prop should set the aria-label for the previous button (`data-direction="previous"`).

### Additional context

This seems to affect all date picker components that use header navigation (DatePicker, MonthPicker, YearPicker, etc.). The labels are being applied to the wrong buttons, which could cause accessibility issues.

---
Repository: /testbed
