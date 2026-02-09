# Bug Report

### Describe the bug

The AskModal component is not showing up when `show()` is called multiple times in quick succession. It seems like there's some kind of throttling happening that prevents the modal from appearing if it's triggered too frequently.

### Reproduction

```js
// Try to show the modal twice quickly
askModalRef.current?.show({
  title: 'First Modal',
  message: 'This should appear',
  onDone: () => console.log('First done')
});

// This one doesn't show up
askModalRef.current?.show({
  title: 'Second Modal', 
  message: 'This should also appear but doesn't',
  onDone: () => console.log('Second done')
});
```

### Expected behavior

Each call to `show()` should display the modal with the provided title and message. If a modal is already open, the new one should either queue up or replace the current one.

### Additional context

This started happening recently. Previously you could call `show()` multiple times and each modal would appear. Now it seems like only the first one shows and subsequent calls within a short time window are ignored.

---
Repository: /testbed
