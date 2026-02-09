# Bug Report

### Describe the bug

The `showGenericModalDialog` method is not passing through dialog options like `tall`, `skinny`, `wide`, and `onHide` to the underlying `dialog()` method. When calling `showGenericModalDialog` with these options, they are being ignored and the dialog always renders with default dimensions and behavior.

### Reproduction

```js
app.showGenericModalDialog('Test Dialog', {
  html: '<p>Dialog content</p>',
  tall: true,
  wide: true,
  onHide: () => console.log('Dialog closed')
});
```

The dialog opens but the `tall` and `wide` options don't affect the dialog size, and the `onHide` callback is never called when the dialog is closed.

### Expected behavior

The dialog should respect the `tall`, `skinny`, `wide`, and `onHide` options passed to `showGenericModalDialog` and forward them to the `dialog()` method so the dialog renders with the correct dimensions and triggers callbacks appropriately.

### System Info

- Insomnia version: latest
- Platform: Cross-platform issue

---
Repository: /testbed
