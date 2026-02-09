# Bug Report

### Describe the bug

I'm encountering an issue with rest parameters in function declarations. When a function has multiple parameters and the last one is a rest parameter, the bundler seems to be treating it incorrectly. The rest parameter doesn't seem to be recognized as such, which causes unexpected behavior.

### Reproduction

```js
function myFunction(a, b, ...rest) {
  console.log(rest);
}

myFunction(1, 2, 3, 4, 5);
// Expected: [3, 4, 5]
// Actual behavior differs
```

Also happens with arrow functions:

```js
const fn = (x, y, ...args) => {
  return args.length;
};

fn(1, 2, 3, 4);
// Should return 2, but behaves unexpectedly
```

### Expected behavior

Rest parameters should be properly identified when they appear as the last parameter in a function signature. The bundler should correctly handle functions with rest parameters regardless of how many regular parameters precede them.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to affect any function that has a rest parameter as the final argument. Not sure if this is a recent regression or if I'm missing something in my configuration.

---
Repository: /testbed
