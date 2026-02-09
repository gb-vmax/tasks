# Bug Report

### Describe the bug

I'm experiencing an issue with template literals in my code. When I use a template literal without any expressions (just a plain string like `` `hello` ``), the bundler seems to be treating it incorrectly during optimization. It appears that simple template literals without interpolations are not being recognized as literal values.

### Reproduction

```js
const simpleTemplate = `hello world`;
console.log(simpleTemplate);

// The bundler doesn't seem to recognize this as a static string value
// This affects tree-shaking and optimization
```

Also noticed that accessing properties on template literal results behaves strangely:

```js
const template = `test`;
const length = template.length; // This interaction seems to be handled incorrectly
```

### Expected behavior

Template literals without any expressions should be treated as static string literals and optimized accordingly. Property access on template literal strings should work the same as regular strings.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
