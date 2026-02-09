# Bug Report

### Describe the bug

After a recent update, the export functionality seems to be broken. When trying to export data, nothing happens and the export dialog doesn't work properly.

### Reproduction

```js
// Attempting to use the export feature
showSelectExportTypeModal({
  onDone: async (selectedFormat) => {
    // This callback never gets called
    console.log('Export format selected:', selectedFormat);
  }
});
```

### Expected behavior

The export modal should display format options and call the `onDone` callback when a format is selected. The callback should receive the selected format and proceed with the export.

### Additional context

It looks like something changed in the `showSelectExportTypeModal` function signature. The function used to accept an `onDone` callback but now it seems like the structure has changed and the callback is no longer being invoked correctly.

This is blocking our ability to export any data from the application.

---
Repository: /testbed
