# Bug Report

### Identifier validation not working correctly

I'm encountering an issue where valid JavaScript identifiers are being rejected and invalid ones are being accepted. It seems like the identifier validation logic is inverted.

### Reproduction

```js
// Valid identifiers are incorrectly rejected
isLegal('myVariable')  // Returns false, but should return true
isLegal('_private')    // Returns false, but should return true
isLegal('$value')      // Returns false, but should return true

// Invalid identifiers are incorrectly accepted
isLegal('123invalid')  // Returns true, but should return false (starts with digit)
isLegal('my-var')      // Returns true, but should return false (contains hyphen)
isLegal('class')       // Returns true, but should return false (reserved word)
```

### Expected behavior

The `isLegal()` function should:
- Return `true` for valid JavaScript identifiers (e.g., `myVariable`, `_private`, `$value`)
- Return `false` for invalid identifiers (e.g., those starting with digits, containing illegal characters, or using reserved words)

This is causing issues when generating code as invalid identifiers are being used without escaping, leading to syntax errors in the output.

---
Repository: /testbed
