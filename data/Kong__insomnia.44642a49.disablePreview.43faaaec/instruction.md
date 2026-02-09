# Bug Report

### Describe the bug

The prompt template tag is not showing previews in certain scenarios where it should. Specifically, when using the prompt tag with a storage key, the preview is being disabled even though the user would expect to see a preview of the stored value.

### Reproduction

```js
// Using prompt with a storage key
{% prompt "Enter value", "default text", "default", "my-storage-key" %}
```

When I use the prompt tag with a storage key parameter, the preview is completely disabled. I would expect to see the last stored value (or default value) in the preview, but instead nothing shows up.

### Expected behavior

The preview should show the stored/default value when a storage key is provided, unless the mask text option is explicitly enabled. The preview should only be disabled when:
- The mask text option is set to true (for sensitive data)
- Other legitimate cases where preview doesn't make sense

Currently it seems like having a storage key automatically disables the preview, which makes it hard to see what value will be used without actually sending the request.

### Additional context

This seems to have changed recently. Previously the preview would show up correctly when using storage keys. Now it's completely hidden which makes debugging template tags much harder.

---
Repository: /testbed
