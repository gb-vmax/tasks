# Bug Report

### Describe the bug

The previous/next navigation buttons in date picker components are not working correctly. When clicking the "previous" button, it seems to trigger the wrong callback or the callbacks are getting mixed up.

### Reproduction

```jsx
const onNext = jest.fn();
const onPrevious = jest.fn();

<DatePickerComponent
  onNext={onNext}
  onPrevious={onPrevious}
/>

// Click the previous button
userEvent.click(screen.getByLabelText('prev'));

// Expected: onPrevious should be called once
// Actual: onNext gets called instead
```

### Expected behavior

- Clicking the "next" button should call the `onNext` callback
- Clicking the "previous" button should call the `onPrevious` callback
- The callbacks should not be swapped or trigger the wrong handler

### Additional context

Also noticed that the `data-static` attribute behavior seems inverted on the level control button. When `hasNextLevel` is `true`, the button has the `data-static` attribute (suggesting it's not interactive), but when `hasNextLevel` is `false`, the attribute is missing (suggesting it is interactive). This seems backwards.

---
Repository: /testbed
