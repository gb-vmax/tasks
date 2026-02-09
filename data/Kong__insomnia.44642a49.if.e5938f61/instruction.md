# Bug Report

### Describe the bug

I'm experiencing an issue where disabled objects are being rendered when they shouldn't be. It seems like the logic for skipping disabled items has been inverted - now enabled objects are being skipped while disabled ones are being processed.

### Reproduction

```js
const disabledItem = {
  name: 'test',
  disabled: true,
  value: '{{variable}}'
}

const enabledItem = {
  name: 'test2',
  disabled: false,
  value: '{{variable}}'
}

// After rendering:
// disabledItem gets rendered (should be skipped)
// enabledItem gets skipped (should be rendered)
```

### Expected behavior

Objects with `disabled: true` should be returned as-is without rendering their template variables. Objects with `disabled: false` or no disabled property should go through the normal rendering process.

### Additional context

This is causing issues in my request configurations where disabled headers/parameters are having their variables interpolated when they should just be ignored completely.

---
Repository: /testbed
