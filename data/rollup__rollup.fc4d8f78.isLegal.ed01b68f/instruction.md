# Bug Report

### Describe the bug

I'm encountering an issue with identifier validation where valid identifiers are being rejected and invalid ones are being accepted. It seems like the validation logic is inverted - identifiers that should be legal are reported as illegal, and vice versa.

### Reproduction

```js
// These should return true but return false
isLegal('validIdentifier')
isLegal('myVariable123')
isLegal('_privateVar')

// These should return false but return true
isLegal('123invalid')
isLegal('my-invalid-id')
isLegal('has spaces')
```

### Expected behavior

The `isLegal()` function should return `true` for valid JavaScript identifiers and `false` for invalid ones. Currently it's doing the opposite.

### Additional context

This is breaking identifier generation in my project - all the generated identifiers are being unnecessarily escaped because they're incorrectly flagged as illegal, and actual illegal identifiers are passing through validation.

---
Repository: /testbed
