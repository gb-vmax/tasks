# Bug Report

### Describe the bug

When using the plugin dialog API with custom actions, the dialog buttons are not rendering correctly. The actions array seems to be processed but the buttons don't appear in the modal dialog.

### Reproduction

```js
app.dialog(
  'Confirm Action',
  document.createElement('div'),
  {
    actions: [
      { label: 'Cancel', onClick: () => console.log('cancelled') },
      { label: 'Confirm', onClick: () => console.log('confirmed'), primary: true }
    ]
  }
);
```

The dialog opens but no action buttons are visible at the bottom. The body content displays normally but the custom actions defined in the options are missing.

### Expected behavior

The dialog should display the custom action buttons at the bottom with proper styling. Primary buttons should use the `btn--clicky` class and all buttons should be laid out horizontally with appropriate spacing.

### Additional context

This seems to have started happening recently. The `onShow` and `onHide` callbacks work as expected, but the actions array doesn't render any buttons. Without the actions, we have no way to close the dialog or trigger the onClick handlers.

---
Repository: /testbed
