# Bug Report

### Describe the bug

I'm experiencing an issue where side effects are not being properly detected in my code. It seems like the bundler is incorrectly caching effect detection results, causing it to skip checking for side effects when it should be re-evaluating them.

### Reproduction

```js
// Module with side effects
console.log('This has side effects');

export function myFunction() {
  // ... code
}
```

When bundling, the side effects are sometimes not detected correctly. The behavior appears inconsistent - sometimes the side effects are properly identified, other times they're ignored even though the code clearly has side effects.

### Expected behavior

The bundler should consistently detect side effects in modules. When a module contains code with side effects (like `console.log`, global mutations, etc.), these should always be recognized and the module should be marked as having effects.

### Additional context

This seems to be related to caching of effect detection. On subsequent builds or when certain conditions are met, the cached result appears to be returned incorrectly, leading to side effects being missed.

---
Repository: /testbed
