# Bug Report

### Describe the bug

The plugin API's `app.dialog()` method is not working correctly. After a recent update, the dialog function seems to have broken syntax - it's not properly defined within the object structure and there are variables/functions declared outside of the method scope that should be inside or properly scoped.

### Reproduction

```js
// Using the plugin API
const plugin = {
  requestHooks: [
    context => {
      // Try to show a dialog
      context.app.dialog('Test Title', document.createElement('div'), {
        onHide: () => console.log('hidden')
      });
    }
  ]
};
```

When trying to use the dialog method, it appears the code structure is malformed. The method definition is not properly contained within the parent object, causing syntax errors.

### Expected behavior

The `app.dialog()` method should be properly defined as a method within the context object and should work as it did before - displaying a modal dialog with the provided title and body content.

### Additional context

Looking at the code, it seems like there's a structural issue where:
- Function declarations are appearing outside of the method
- The `dialog` method definition appears to be incorrectly positioned
- Variables like `dialogIdCounter` and `dialogRegistryMap` are declared in the wrong scope

This is preventing the plugin system from loading correctly.

---
Repository: /testbed
