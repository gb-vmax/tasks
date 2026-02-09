# Bug Report

### Describe the bug

I'm encountering an issue with switch statements where the discriminant expression seems to be parsed with the wrong scope. This is causing variables referenced in the switch discriminant to not be resolved correctly, leading to incorrect behavior during code analysis.

### Reproduction

```js
function test() {
  const value = getSomeValue();
  
  switch (value) {
    case 1:
      console.log('one');
      break;
    case 2:
      console.log('two');
      break;
  }
}
```

In this example, the `value` variable in the switch discriminant is not being resolved properly. It appears that the discriminant is being parsed with an incorrect parent scope, which breaks variable resolution and potentially causes issues with tree-shaking and other optimizations.

### Expected behavior

The discriminant expression should be parsed using the correct scope so that variable references are properly resolved. This should allow for correct static analysis of the switch statement and its dependencies.

### Additional context

This seems to affect any switch statement where the discriminant references variables from the enclosing scope. The issue appears to be related to how the discriminant node is being constructed and which scope is being passed to it during parsing.

---
Repository: /testbed
