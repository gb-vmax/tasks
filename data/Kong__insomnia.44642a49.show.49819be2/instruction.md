# Bug Report

### Describe the bug

After a recent update, the prompt modal is broken - it doesn't show up when triggered. The modal should appear when calling the `show` method but nothing happens.

### Reproduction

```js
// Try to open the prompt modal
promptModalRef.current?.show({
  title: 'Enter name',
  defaultValue: 'test',
  onComplete: (value) => {
    console.log(value);
  }
});

// Expected: Modal appears
// Actual: Nothing happens, modal doesn't show
```

### Steps to reproduce
1. Trigger a prompt modal in the application
2. The modal fails to appear
3. No errors in console

### Expected behavior
The prompt modal should display when the `show` method is called with valid options.

### Additional context
This seems to have broken recently. The modal was working fine before but now it just doesn't render at all. Looks like there might be an issue with how the show method is structured or something with the syntax.

---
Repository: /testbed
