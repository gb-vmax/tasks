# Bug Report

### Describe the bug

I'm encountering a syntax error when trying to use the interpolator with faker functions. It looks like there's an issue with the code structure - methods are being defined outside of the class body which causes the application to fail at runtime.

### Reproduction

```js
const interpolator = new Interpolator();

// This throws an error when the module is loaded
const result = interpolator.render('{{$firstName}}', {});
```

The error occurs immediately when trying to instantiate or use the Interpolator class because the helper methods `getFakerCacheKey` and `invokeFakerFunction` are declared with `private` keyword but placed outside the class definition.

### Expected behavior

The interpolator should work correctly and be able to render templates with faker functions. The helper methods should be properly defined as part of the class.

### System Info
- insomnia-sdk version: latest
- Node.js version: 18.x

This seems like it might have been introduced in a recent refactoring. The code compiles but fails at runtime due to the incorrect method placement.

---
Repository: /testbed
