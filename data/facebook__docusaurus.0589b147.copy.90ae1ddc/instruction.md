# Bug Report

### Describe the bug
When using the `copy()` method on a processor instance, the copied processor doesn't properly inherit the configuration data from the original processor. Changes made to nested properties in the original processor's namespace seem to affect the copied processor as well, which shouldn't happen according to the documentation that states "When the descendant processor is configured in the future it does not affect the ancestral processor."

### Reproduction
```js
const originalProcessor = new Processor();

// Configure original processor with nested data
originalProcessor.data('settings', {
  options: {
    value: 'original'
  }
});

// Create a copy
const copiedProcessor = originalProcessor.copy();

// Modify the original processor's nested data
originalProcessor.data('settings').options.value = 'modified';

// The copied processor's data is also affected
console.log(copiedProcessor.data('settings').options.value);
// Expected: 'original'
// Actual: 'modified'
```

### Expected behavior
The copied processor should have a completely independent copy of the namespace data. Modifications to nested properties in the original processor should not affect the copied processor.

### Additional context
This appears to be related to how the namespace data is being copied - it seems like a shallow copy is being performed instead of a deep copy, causing nested objects to still reference the same memory locations.

---
Repository: /testbed
