# Bug Report

### Describe the bug

When rendering objects with the `disabled` property set to `true`, they are being processed and rendered instead of being skipped. This is the opposite of the expected behavior - disabled objects should be returned as-is without any rendering applied to them.

### Reproduction

```js
const disabledObject = {
  disabled: true,
  value: '{{ template_variable }}',
  name: 'test'
};

const result = await render(disabledObject);
// Expected: { disabled: true, value: '{{ template_variable }}', name: 'test' }
// Actual: The template variable gets rendered even though the object is disabled
```

### Expected behavior

Objects with `disabled: true` should be returned immediately without any rendering logic applied to them. The current behavior appears to be inverted - it's only returning disabled objects and processing everything else, when it should be the other way around.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
