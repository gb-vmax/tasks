# Bug Report

### Describe the bug

The interpolator is not rendering templates correctly. When trying to use the `render()` method, it throws an error because the engine is not properly initialized.

### Reproduction

```js
const interpolator = new Interpolator({ autoescape: false });

// This throws an error
const result = interpolator.render('Hello {{ name }}', { name: 'World' });
```

### Expected behavior

The `render()` method should successfully interpolate the template with the provided context and return `'Hello World'`.

### Additional context

This seems to have broken recently. The interpolator was working fine before but now fails when trying to render any template string.

---
Repository: /testbed
