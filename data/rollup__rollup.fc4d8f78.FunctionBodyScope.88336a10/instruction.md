# Bug Report

### Describe the bug

I'm encountering an issue with function parameter redeclaration in function scopes. When I try to redeclare a function parameter using `var` or `function` declaration, I'm getting an error even though this should be allowed in JavaScript.

### Reproduction

```js
function example(x) {
  var x = 10; // This should be allowed but throws an error
  console.log(x);
}

function test(y) {
  function y() {} // This should also be allowed but throws an error
}
```

### Expected behavior

In JavaScript, function parameters can be redeclared with `var` or `function` declarations within the function body. This is valid ES5/ES6 behavior and should not throw an error. The redeclaration should shadow the parameter.

For example:
```js
function foo(a) {
  var a = 5; // valid - should not error
  return a;
}
foo(1); // returns 5
```

### Additional context

This seems to have started recently. The error message indicates a redeclaration error, but according to JavaScript semantics, parameters can be redeclared with `var` and `function` declarations in the same scope.

---
Repository: /testbed
