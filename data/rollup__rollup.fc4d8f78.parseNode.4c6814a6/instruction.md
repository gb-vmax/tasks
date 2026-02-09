# Bug Report

### Describe the bug

I'm experiencing an issue with switch statement scoping. When using variables in a switch discriminant (the expression being switched on), they're not being resolved correctly in certain cases. It seems like the discriminant expression is being evaluated in the wrong scope context.

### Reproduction

```js
function test() {
  const value = 5;
  
  switch (value + 1) {
    case 6:
      console.log('matched');
      break;
    default:
      console.log('not matched');
  }
}
```

In this example, the discriminant `value + 1` should have access to the `value` variable from the parent scope, but it appears to be looking in the wrong scope. This causes issues with variable resolution in the discriminant expression.

### Expected behavior

The discriminant expression should be evaluated in the parent scope of the switch statement, allowing it to access variables declared in the containing function or block. Variables used in the discriminant should resolve correctly just like they would in any other expression at that position.

### Additional context

This seems to affect any switch statement where the discriminant references variables from the surrounding scope. The issue is particularly noticeable when the discriminant contains complex expressions or function calls that depend on locally scoped variables.

---
Repository: /testbed
