# Bug Report

### Describe the bug

I'm encountering an issue with assignment patterns in function parameters. The generated code has the default value appearing before the parameter name, which results in invalid JavaScript syntax.

### Reproduction

When processing code with default parameters like this:

```js
function example(param = 'default') {
  console.log(param);
}
```

The output is generating something like:

```js
function example( = 'default'param) {
  console.log(param);
}
```

The parameter name and its default value are in the wrong order.

### Expected behavior

The generated code should maintain the correct syntax with the parameter name first, followed by the assignment operator and default value:

```js
function example(param = 'default') {
  console.log(param);
}
```

This appears to affect any function or arrow function that uses default parameter values. The generated output is not valid JavaScript and causes syntax errors when executed.

---
Repository: /testbed
