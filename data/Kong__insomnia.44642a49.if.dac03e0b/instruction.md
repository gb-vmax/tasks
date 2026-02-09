# Bug Report

### Describe the bug

I'm experiencing an issue where disabled objects are being returned as `undefined` during rendering, while enabled objects are being returned without any rendering applied. This is the opposite of what should happen.

### Reproduction

```js
const disabledObject = {
  disabled: true,
  name: 'test',
  url: '{{ base_url }}/endpoint'
};

const enabledObject = {
  disabled: false,
  name: 'test',
  url: '{{ base_url }}/endpoint'
};

// After rendering:
// disabledObject is returned as-is (expected)
// enabledObject is returned as undefined (unexpected - should be rendered)
```

### Expected behavior

- Objects with `disabled: true` should be returned as-is without rendering
- Objects with `disabled: false` (or without the disabled property) should go through the normal rendering process and have their template variables resolved

### Current behavior

The behavior appears to be inverted - disabled objects are being filtered out while enabled objects are being returned without rendering.

This is causing issues where valid configuration objects are disappearing during the render phase, breaking functionality that depends on template variable resolution.

---
Repository: /testbed
