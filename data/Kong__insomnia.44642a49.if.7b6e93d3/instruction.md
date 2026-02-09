# Bug Report

### Describe the bug

I'm experiencing an issue with object rendering where properties with underscores anywhere in their name are not being processed correctly. It seems like the rendering logic is skipping path tracking for any property that contains an underscore character, not just those that start with an underscore.

### Reproduction

```js
const obj = {
  normal_property: '{{ someVar }}',
  another_field: '{{ anotherVar }}',
  regularField: '{{ thirdVar }}'
}

// After rendering, properties with underscores in the middle 
// don't get the correct path context
await render(obj, context)
```

### Expected behavior

Properties should only skip path tracking if they start with an underscore (private/internal fields). Properties like `normal_property` or `some_field` that contain underscores in the middle should be processed with their full path like any other property.

Currently it looks like the condition is checking if an underscore exists anywhere in the key name (`indexOf('_') !== -1`) instead of checking if it starts with one (`indexOf('_') === 0`).

### Additional context

This is affecting template variable resolution for any object properties that use snake_case naming convention. The rendering works but the path context is lost for these properties.

---
Repository: /testbed
