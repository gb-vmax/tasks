# Bug Report

### Describe the bug
The modal show method is not working properly after recent changes. When trying to open a modal, it doesn't appear and the application seems to hang or become unresponsive. This appears to be related to the async handling of the show method.

### Reproduction
```js
// Try to show a modal with simple options
modalRef.current?.show({
  title: 'Test Modal',
  body: <div>Modal content</div>
});

// Modal doesn't appear
```

The issue seems to happen consistently when calling the show method. Previously this worked fine, but now the modal just won't display.

### Expected behavior
The modal should open immediately when `show()` is called with the provided options.

### Additional context
This started happening after some recent updates to the wrapper-modal component. The modal worked correctly before and now it just doesn't show up at all.

---
Repository: /testbed
