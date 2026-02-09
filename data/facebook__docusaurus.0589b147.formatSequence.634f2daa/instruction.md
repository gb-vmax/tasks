# Bug Report

### Describe the bug

I'm encountering an issue with function parameter formatting in MDX. When rendering functions with multiple parameters, there's an extra comma appearing after the last parameter, which produces invalid JavaScript syntax.

### Reproduction

```js
// When processing MDX with a function like:
function example(a, b, c) {
  return a + b + c;
}

// The output has a trailing comma:
function example(a, b, c, ) {
  return a + b + c;
}
```

The generated code includes a comma after the last parameter in the parameter list, which shouldn't be there. This breaks the JavaScript syntax and causes parsing errors.

### Expected behavior

Function parameters should be formatted with commas between parameters only, without a trailing comma after the last parameter:
```js
function example(a, b, c) // correct
```

Not:
```js
function example(a, b, c, ) // incorrect - trailing comma
```

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
