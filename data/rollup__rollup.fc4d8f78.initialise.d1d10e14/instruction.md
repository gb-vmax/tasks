# Bug Report

### Describe the bug

I'm experiencing an issue where reassigning to non-const variables is incorrectly triggering warnings about const reassignment. The bundler is logging warnings for regular `let` and `var` variable assignments, which shouldn't happen.

### Reproduction

```js
let count = 0;
count = 5; // This incorrectly triggers a const reassignment warning

var name = 'test';
name = 'updated'; // This also triggers the warning incorrectly
```

The warning message appears during bundling even though these are not const variables.

### Expected behavior

Only actual const variable reassignments should trigger the const reassignment warning. Regular `let` and `var` assignments should work without any warnings.

```js
const value = 10;
value = 20; // This SHOULD trigger the warning

let count = 0;
count = 5; // This should NOT trigger any warning
```

### Additional context

This seems to have started recently. The bundler is now treating all variable assignments as if they were const reassignments, which is causing a lot of false positive warnings in my codebase.

---
Repository: /testbed
