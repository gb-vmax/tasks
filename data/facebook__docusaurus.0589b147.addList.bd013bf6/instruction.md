# Bug Report

### Describe the bug

I'm encountering an issue with the remark processor where passing a single plugin (not in an array) causes unexpected behavior. It seems like the plugin gets executed during the validation phase instead of being properly registered.

### Reproduction

```js
const processor = remark();

// This doesn't work as expected anymore
processor.use(somePlugin);

// Only this works now
processor.use([somePlugin]);
```

When I pass a plugin directly (without wrapping it in an array), the plugin appears to be called immediately during the `use()` method instead of being added to the plugin list. This is different from the previous behavior where both syntaxes worked correctly.

### Expected behavior

Both of these should work the same way:
- `processor.use(plugin)` - single plugin
- `processor.use([plugin])` - array with one plugin

The plugin should be registered and executed during processing, not during the registration phase.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
