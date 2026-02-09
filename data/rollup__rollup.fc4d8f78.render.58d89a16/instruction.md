# Bug Report

### Describe the bug

I'm encountering an issue with return statements in my bundled code. When a return statement has an argument that starts immediately after the `return` keyword (without whitespace), the bundler is incorrectly adding a space between them even when there's already whitespace present.

### Reproduction

```js
// Input code
function test() {
  return (
    someValue
  );
}
```

After bundling, the output becomes malformed with extra spacing where it shouldn't be:

```js
function test() {
  return  (
    someValue
  );
}
```

The space is being inserted in the wrong condition - it's adding space when there IS already whitespace/newline between `return` and the argument, instead of when there ISN'T.

### Expected behavior

The bundler should only add a space when the argument directly follows the `return` keyword without any whitespace, like:

```js
return(value)  // Should become: return (value)
```

But it should NOT add a space when there's already whitespace:

```js
return (value)  // Should stay: return (value)
```

This seems to have broken recently and is affecting code with multi-line return statements.

---
Repository: /testbed
