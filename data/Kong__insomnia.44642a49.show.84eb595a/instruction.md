# Bug Report

### Describe the bug

After a recent update, the prompt modal is not working correctly. When I try to open the modal, it fails to appear and the application seems to hang or behave unexpectedly.

### Reproduction

```js
// Try to open a prompt modal
promptModalRef.current?.show({
  title: 'Enter value',
  defaultValue: 'test',
  onComplete: (value) => {
    console.log('Submitted:', value);
  }
});
```

The modal doesn't show up and the UI becomes unresponsive.

### Expected behavior

The prompt modal should open normally and allow user input. After submitting, the `onComplete` callback should be triggered with the entered value.

### Additional context

This seems to have started happening after some changes to the prompt modal component. The modal was working fine in the previous version. It looks like there might be an issue with how the `show` method is structured or how the component handles its internal state.

---
Repository: /testbed
