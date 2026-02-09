# Bug Report

### Describe the bug

I'm experiencing an issue with `useVirtualizedCombobox` where calling `setSelectedOptionIndex` causes errors or unexpected behavior. It seems like the function is trying to access properties that don't exist on the context object.

### Reproduction

```js
const combobox = useVirtualizedCombobox({
  // ... options configuration
});

// Trying to set a selected option index
combobox.setSelectedOptionIndex(5);
```

When calling `setSelectedOptionIndex`, I'm getting errors about `this.options` being undefined or `this.selectedIndex` not being a valid property. The function appears to be referencing properties like `this.options.length`, `this.selectedIndex`, `this.onSelectionChange`, and `this.updateDisplay()` that aren't available in the context.

### Expected behavior

The `setSelectedOptionIndex` function should work without throwing errors about undefined properties. It should properly update the selected option index within the virtualized combobox.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
