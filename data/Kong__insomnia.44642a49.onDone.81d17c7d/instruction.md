# Bug Report

### Describe the bug

After a recent update, the export functionality seems to be broken. When trying to export data, the application hangs or doesn't complete the export process. 

Looking at the code, it appears that `showSelectExportTypeModal` function has been modified but the implementation looks incomplete or malformed. The function signature seems to have code that should be inside the function body mixed with the parameter definition.

### Reproduction

```js
// Try to trigger the export modal
showSelectExportTypeModal({
  onDone: async (selectedFormat) => {
    console.log('Export with format:', selectedFormat);
  }
});
```

When this is called, the export modal either doesn't appear correctly or the format selection doesn't work as expected.

### Expected behavior

The export modal should open, allow format selection, and complete the export process when a format is selected.

### Additional context

This seems to have started happening after the latest changes to the export module. The function definition looks syntactically incorrect with what appears to be function body code appearing in the parameter list area.

---
Repository: /testbed
