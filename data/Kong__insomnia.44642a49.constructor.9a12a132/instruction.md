# Bug Report

### Describe the bug
The interpolator is throwing errors when trying to render templates. After initializing an `Interpolator` instance, calling the `render` method results in a crash because the internal engine is not properly set up.

### Reproduction
```js
const interpolator = new Interpolator(config);

// This throws an error
const result = interpolator.render('Hello {{ name }}', { name: 'World' });
```

### Expected behavior
The template should be rendered successfully and return `'Hello World'`. The interpolator should work after being instantiated with a valid configuration.

### Additional context
This seems to have broken recently. The interpolator was working fine before but now fails immediately when trying to render any template string.

---
Repository: /testbed
