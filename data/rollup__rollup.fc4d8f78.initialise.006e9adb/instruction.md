# Bug Report

### Describe the bug

I'm getting warnings about reassigning const variables when I'm actually reassigning regular variables (let/var). The warning should only appear when trying to reassign actual const variables, but it seems to be triggered incorrectly.

### Reproduction

```js
let myVariable = 10;
myVariable = 20; // This triggers a const reassignment warning incorrectly
```

The code above should work fine without any warnings since `myVariable` is declared with `let`, not `const`. However, I'm seeing a warning message about trying to reassign a const variable.

### Expected behavior

- Reassigning `let` or `var` variables should NOT produce any warnings
- Only reassigning actual `const` variables should trigger the const reassignment warning

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
