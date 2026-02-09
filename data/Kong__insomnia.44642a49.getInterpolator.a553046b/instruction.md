# Bug Report

### Describe the bug
When trying to use the interpolator in my scripts, I'm getting an error that says the interpolator is undefined. It seems like `getInterpolator()` is returning `undefined` instead of the actual interpolator object.

### Reproduction
```js
const interpolator = getInterpolator();

// This throws an error because interpolator is undefined
interpolator.render('{{ variable }}', context);
```

### Expected behavior
`getInterpolator()` should return a valid interpolator instance that can be used to render templates with variables.

### System Info
- Insomnia SDK version: latest
- Node version: 18.x

---
Repository: /testbed
