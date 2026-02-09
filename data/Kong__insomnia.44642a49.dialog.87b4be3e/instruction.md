# Bug Report

### Describe the bug

I'm experiencing an issue with the plugin dialog API where the dialog modal closes immediately or doesn't display properly when using certain options. It seems like something is broken with the dialog rendering after a recent update.

### Reproduction

```js
// Using the plugin API to show a dialog
app.dialog(
  'My Dialog',
  document.createElement('div'),
  {
    tall: true,
    onHide: () => console.log('Dialog closed')
  }
);
```

When I call this, the dialog either doesn't appear at all or closes right away. The behavior is inconsistent and it's affecting my plugin functionality.

### Expected behavior

The dialog should open and display the content properly, staying open until the user dismisses it. The `onHide` callback should only be called when the dialog is actually closed by the user.

### Additional context

This was working fine before but now it's broken. I noticed this happens specifically when trying to use the dialog during request sending or in certain render contexts. The dialog just doesn't stay open like it used to.

---
Repository: /testbed
