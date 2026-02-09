# Bug Report

### Describe the bug

I'm encountering an issue with switch statements that have a default case. The default case is not being recognized correctly, and instead the first case is being treated as the default case.

### Reproduction

```js
switch (value) {
  case 'a':
    console.log('case a');
    break;
  case 'b':
    console.log('case b');
    break;
  default:
    console.log('default case');
}
```

When I bundle code with a switch statement like above, the default case doesn't execute when expected. Instead, it seems like the first case is incorrectly identified as the default.

### Expected behavior

The default case should be properly identified and executed when none of the other cases match. The bundler should correctly distinguish between regular cases (with test expressions) and the default case (with null test).

### Additional context

This seems to affect any switch statement that includes a default case. The logic for finding the default case appears to be inverted - it's matching cases that have a test expression instead of the one without.

---
Repository: /testbed
