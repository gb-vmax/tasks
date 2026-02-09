# Bug Report

### Describe the bug

When declaring variables with `var` or `function` that have the same name as existing variables (also `var`, `function`, or parameters), the code is creating duplicate variable entries instead of reusing the existing variable. This causes issues with variable hoisting and scope resolution.

### Reproduction

```js
function test(x) {
  var x = 5;  // Should reuse parameter 'x', but creates new variable instead
  console.log(x);
}

// or

function example() {
  var foo = 1;
  var foo = 2;  // Should reuse existing 'foo', but creates duplicate
  return foo;
}

// or

function demo() {
  function bar() {}
  function bar() {}  // Function redeclaration should reuse existing, but creates new entry
}
```

### Expected behavior

When a `var` or `function` declaration has the same name as an existing `var`, `function`, or `parameter`, it should reuse the existing variable entry and just add the new declaration to it. The function should return the existing variable instead of creating a new one.

### Additional context

This appears to be a scope management issue where valid redeclarations (which JavaScript allows for `var` and `function`) are not being handled correctly. The existing variable should be returned when the redeclaration is valid, but instead a new variable is always being created and added to the scope.

---
Repository: /testbed
