# Bug Report

### Describe the bug

I'm encountering an issue with anonymous function declarations in my code. When I use a function declaration without a name (like `export default function() { ... }`), the bundler crashes with a null reference error.

### Reproduction

```js
// This causes a crash
export default function() {
  return 'hello world';
}
```

The error occurs during the parsing/analysis phase. Named function declarations work fine:

```js
// This works correctly
export default function myFunction() {
  return 'hello world';
}
```

### Expected behavior

Anonymous function declarations should be handled gracefully without crashing. This is valid JavaScript syntax and should be supported.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
