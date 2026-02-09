# Bug Report

### Describe the bug

The `showGenericModalDialog` method is not passing through dialog options correctly. When using options like `tall`, `skinny`, `wide`, or `onHide`, they are being ignored and the dialog always displays with default sizing/behavior.

### Reproduction

```js
app.showGenericModalDialog(
  'My Dialog',
  {
    html: '<p>Dialog content</p>',
    tall: true,
    onHide: () => console.log('Dialog closed')
  }
);
```

The dialog opens but:
- The `tall` option has no effect - dialog uses default height
- The `onHide` callback never gets called when closing the dialog

### Expected behavior

The dialog should respect the provided options (`tall`, `skinny`, `wide`, `onHide`) and pass them through to the underlying `dialog()` method, just like it did before.

### Additional context

This is affecting plugins that rely on the deprecated `showGenericModalDialog` API. While I understand this method is deprecated, it should still work correctly until it's fully removed.

---
Repository: /testbed
