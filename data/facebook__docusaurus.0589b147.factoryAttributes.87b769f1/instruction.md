# Bug Report

### Describe the bug

I'm encountering an issue with directive attribute parsing where the token tree structure appears to be malformed. When parsing directives with attributes that include values (using the `=` sign), the attribute type token is not being properly closed before the initializer is entered.

### Reproduction

```js
// Parsing a directive with an attribute assignment
::directive{attr=value}

// The token tree structure is incorrect - the attributeType 
// token remains open when entering the attributeInitializerType
```

### Expected behavior

The token tree should have a properly nested structure where:
1. `attributeType` is entered
2. Attribute name tokens are processed
3. `attributeType` is exited **before** entering `attributeInitializerType`
4. The initializer (equals sign) is processed
5. The value is parsed

Currently, the `attributeType` token is not being closed at the right time, leading to an improperly nested token structure.

### Additional context

This affects any directive that uses the attribute assignment syntax with `=`. The token stream doesn't maintain the correct hierarchy, which could cause issues downstream when processing the AST.

---
Repository: /testbed
