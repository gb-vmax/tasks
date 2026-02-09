# Bug Report

### Describe the bug

The AskModal component is broken after a recent update. When trying to use the modal, it doesn't display properly and the buttons don't respond to clicks. The modal appears to be in some kind of broken state where it can't properly handle user interactions.

### Reproduction

```jsx
import { AskModal } from './components/modals/ask-modal';

// Try to show a confirmation dialog
askModalRef.current?.show({
  title: 'Confirm Action',
  message: 'Are you sure you want to proceed?',
  yesText: 'Proceed',
  noText: 'Cancel',
  onDone: (success) => {
    console.log('User clicked:', success ? 'Yes' : 'No');
  }
});
```

### Expected behavior

The modal should display with the title and message, and clicking either button should trigger the `onDone` callback with the appropriate boolean value. The modal should then close.

### Actual behavior

The modal either doesn't show up at all or shows up but the buttons are unresponsive. It seems like there's a syntax or structural issue with the component code itself.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking our workflow as we can't show any confirmation dialogs to users. Would appreciate a quick fix!

---
Repository: /testbed
