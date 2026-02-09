# Bug Report

### Describe the bug

When using the `AskModal` component, the modal seems to have issues with its callback handling. The `onDone` callback is being triggered unexpectedly when the modal is closed programmatically via the `hide()` method, even when the user hasn't clicked any button.

### Reproduction

```jsx
const askModalRef = useRef();

// Show the modal with an onDone callback
askModalRef.current?.show({
  title: 'Confirm Action',
  message: 'Are you sure?',
  onDone: (success) => {
    console.log('User clicked:', success ? 'Yes' : 'No');
  }
});

// Later, close the modal programmatically
askModalRef.current?.hide();

// The onDone callback gets called with false, even though 
// the user never clicked any button
```

### Expected behavior

The `onDone` callback should only be invoked when the user explicitly clicks one of the action buttons (Yes/No). When the modal is closed programmatically using `hide()`, the callback should not be triggered since no user decision was made.

### Additional context

This appears to be a regression - the modal used to work correctly where programmatic closes wouldn't trigger the callback. Now it's causing issues in our application where we need to programmatically dismiss the modal in certain scenarios without treating it as a user action.

---
Repository: /testbed
