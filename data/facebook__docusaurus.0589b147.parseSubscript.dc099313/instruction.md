# Bug Report

### Describe the bug

After a recent update, I'm getting syntax errors when trying to parse JavaScript code that contains optional chaining with function calls. The parser seems to be unable to handle expressions like `obj?.method()` or `obj?.[prop]()`.

### Reproduction

```js
// This code fails to parse:
const result = obj?.method();

// This also fails:
const value = obj?.[key]();

// Even simple optional chaining with property access doesn't work:
const data = user?.profile?.name;
```

When trying to parse any code with optional chaining operators (`?.`), the parser throws an error or produces incorrect output.

### Expected behavior

The parser should correctly handle optional chaining syntax, which is valid JavaScript (ES2020/ES11+). These expressions should parse without errors:
- `obj?.prop`
- `obj?.method()`
- `obj?.[computed]`
- Nested optional chaining like `a?.b?.c`

### System Info
- ECMAScript version: ES2020 (ES11)
- Parser options: ecmaVersion >= 11

This is blocking our ability to parse modern JavaScript code that uses optional chaining. Any help would be appreciated!

---
Repository: /testbed
