# Bug Report

### Describe the bug

I'm encountering an issue where identifiers that should be considered illegal/invalid are being accepted as legal, and vice versa. It seems like the validation logic for identifier names has been inverted somehow.

### Reproduction

```js
// These should be illegal but are passing validation
isLegal('123abc')  // returns true (should be false - starts with number)
isLegal('my-var')  // returns true (should be false - contains hyphen)
isLegal('class')   // returns true (should be false - reserved keyword)

// These should be legal but are failing validation
isLegal('myVar')   // returns false (should be true)
isLegal('_private') // returns false (should be true)
isLegal('$value')  // returns false (should be true)
```

### Expected behavior

The `isLegal()` function should correctly identify valid identifiers and reject invalid ones according to JavaScript naming rules. Valid identifiers should return `true`, and invalid identifiers (those starting with numbers, containing illegal characters, or matching reserved keywords) should return `false`.

### System Info
- Version: latest from main branch
- Node: v18.x

This is blocking me from properly validating user input for variable names in my code generator. Any help would be appreciated!

---
Repository: /testbed
