# Bug Report

### Describe the bug

The AskModal component is not displaying when I try to show it with a message. After a recent update, calling `show()` on the modal doesn't seem to work anymore and nothing happens.

### Reproduction

```jsx
const askModalRef = useRef();

// Later in the code...
askModalRef.current?.show({
  title: 'Confirm Action',
  message: 'Are you sure you want to proceed?',
  onDone: async (success) => {
    console.log('User clicked:', success);
  }
});
```

The modal doesn't appear on screen. I've also noticed that if I try to pass an empty string as the message, it still doesn't show up but there's no feedback about what went wrong.

### Expected behavior

The modal should display with the provided title and message, allowing the user to click Yes or No buttons.

### Additional context

This was working fine before. I'm using the AskModal in several places in my app and they all stopped working after updating. The modal reference seems to be set correctly, but the `show()` method doesn't trigger the modal to appear.

---
Repository: /testbed
