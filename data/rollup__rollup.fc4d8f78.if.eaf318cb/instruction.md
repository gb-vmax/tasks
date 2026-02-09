# Bug Report

### Describe the bug

I'm encountering an issue with global variable names in the generated output. When a global variable is assigned a falsy value (like `0`, `false`, or empty string), it's not being rendered correctly in the output. Instead of using the global name, the code falls through and uses a different naming strategy.

### Reproduction

```js
// When a variable has globalName set to 0 or false
const variable = {
  globalName: 0,
  name: 'someVariable'
}

// The getName() method should return "0" but it doesn't
// It falls through to other naming logic instead
```

This seems to affect any falsy global name values:
- `globalName: 0` 
- `globalName: false`
- `globalName: ""`

### Expected behavior

When `globalName` is set to any value (including falsy ones like `0` or `false`), it should be converted to a string and returned. The current implementation only checks truthiness which causes falsy but valid values to be ignored.

### System Info
- Version: Latest main branch
- Node: v18.x

---
Repository: /testbed
