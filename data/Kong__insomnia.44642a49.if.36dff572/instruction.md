# Bug Report

### Describe the bug

I'm experiencing an issue with the rendering system where object properties with underscores are not being processed correctly. It seems like properties that start with an underscore (like `_id`, `_type`, etc.) are being handled differently than they should be, and this is affecting how nested objects are rendered.

### Reproduction

```js
const obj = {
  _id: '{{ someVariable }}',
  name: '{{ anotherVariable }}',
  nested: {
    _internal: '{{ nestedVariable }}'
  }
}

// After rendering, underscore-prefixed properties 
// are not being interpolated as expected
const result = await render(obj);
```

### Expected behavior

All properties, regardless of whether they start with an underscore or not, should be rendered/interpolated consistently. The underscore prefix shouldn't affect how the rendering logic processes the property values.

### Additional context

This seems to have started happening recently. Previously, properties with underscores were being handled the same way as regular properties. Now there's some inconsistency in how they're being processed during the render pass.

---
Repository: /testbed
