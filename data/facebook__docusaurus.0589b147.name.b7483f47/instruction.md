# Bug Report

### Describe the bug

I'm experiencing an issue with identifier name validation in MDX. It seems like the logic for determining valid names based on JSX mode has been inverted - names that should be valid are being rejected and vice versa.

### Reproduction

```js
// When jsx option is enabled, regular JSX identifiers are being rejected
const options = { jsx: true };
const result = name('myComponent', options);
// Returns false when it should return true

// When jsx option is disabled or not provided, it's using JSX rules instead
const result2 = name('myComponent', {});
// Uses JSX validation rules when it shouldn't
```

### Expected behavior

- When `jsx: true` is set in options, JSX identifier rules should be applied
- When `jsx` is false or options are not provided, standard identifier rules should be applied
- Valid component names should pass validation based on the correct rule set

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
