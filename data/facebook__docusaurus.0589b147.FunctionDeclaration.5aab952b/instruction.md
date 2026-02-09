# Bug Report

### Describe the bug

When generating code for function declarations, there's an issue with spacing before the function body. The space is only being added for async functions, but it should be added for all function types (regular, async, and generator functions).

### Reproduction

```js
// For a regular function declaration:
function myFunction() {
  return true;
}

// For a generator function:
function* myGenerator() {
  yield 1;
}
```

After code generation, these functions are missing the space between the parameter list and the opening brace of the function body, resulting in output like:

```js
function myFunction(){
  return true;
}

function* myGenerator(){
  yield 1;
}
```

Only async functions have the correct spacing:
```js
async function myAsyncFunction() {
  return true;
}
```

### Expected behavior

All function declarations (regular, async, and generator) should have a space between the closing parenthesis of the parameter list and the opening brace of the function body.

The generated code should look like:
```js
function myFunction() {
  return true;
}
```

Not:
```js
function myFunction(){
  return true;
}
```

---
Repository: /testbed
