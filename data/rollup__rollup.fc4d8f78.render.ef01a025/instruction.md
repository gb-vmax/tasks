# Bug Report

### Describe the bug

I'm encountering an issue with `throw` statement rendering where the space between `throw` and the argument is not being inserted correctly. This results in invalid JavaScript output that produces syntax errors.

### Reproduction

```js
// When bundling code with a throw statement like:
throw new Error('message');

// The output is missing the space:
thrownew Error('message');
```

This creates invalid JavaScript that fails to parse. The issue seems to affect throw statements where the argument immediately follows the keyword.

### Expected behavior

The bundler should always ensure there's a space between the `throw` keyword and its argument, producing valid JavaScript:

```js
throw new Error('message');
```

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
