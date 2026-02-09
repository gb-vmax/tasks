# Bug Report

### Describe the bug

After a recent update, the plugin dialog system is not working correctly. When I call `app.dialog()` from a plugin, it's returning an object with `id` and `dismiss` properties, but my plugin code expects `dialog()` to return `undefined` (or nothing). This is breaking compatibility with existing plugins.

### Reproduction

```js
// In a plugin
module.exports.requestHooks = [
  context => {
    // This used to work fine
    context.app.dialog(
      'My Dialog',
      document.createElement('div'),
      {
        onHide: () => console.log('Dialog closed')
      }
    );
    
    // Now it returns { id: '...', dismiss: Function }
    // which breaks code that expects no return value
  }
];
```

### Expected behavior

The `app.dialog()` method should not return anything (or return `undefined`) to maintain backward compatibility with existing plugins. Many plugins don't expect a return value from this method.

### System Info
- Insomnia version: latest
- Plugin API context: app

This seems like it might be a breaking change that was introduced without updating the plugin API documentation. Could we either revert this or provide a migration path for existing plugins?

---
Repository: /testbed
