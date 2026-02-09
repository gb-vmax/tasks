# Bug Report

### Describe the bug

I'm experiencing an issue with the rendering system where objects with `disabled: false` are being skipped during rendering. It seems like the renderer is treating `disabled: false` the same as `disabled: true`, which prevents these objects from being processed.

### Reproduction

```js
const obj = {
  name: 'test-object',
  disabled: false,
  value: '{{ variable }}'
}

// This object should be rendered since disabled is explicitly false
const result = await render(obj)

// Expected: obj.value is rendered with variable substitution
// Actual: obj is returned as-is without rendering
```

### Expected behavior

Objects with `disabled: false` should be rendered normally. Only objects with `disabled: true` (or a truthy disabled value) should be skipped.

### Additional context

This affects any workflow where objects need to explicitly set `disabled: false` to ensure they're processed. The current behavior makes it impossible to render objects that have the disabled property set to false.

---
Repository: /testbed
