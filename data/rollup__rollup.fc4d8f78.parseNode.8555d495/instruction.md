# Bug Report

### Describe the bug

I'm encountering an issue with function declarations where the identifier scope seems to be incorrectly resolved. When parsing function declarations with named identifiers, the scope chain appears to be broken or pointing to the wrong parent scope.

### Reproduction

```js
function myFunction() {
  // Function body
}

// The function identifier 'myFunction' is not being resolved correctly
// in the scope chain during parsing
```

This seems to affect how function names are registered and looked up in their containing scope. The problem appears when the AST is being constructed and function identifiers need to reference their proper scope.

### Expected behavior

Function declaration identifiers should be correctly associated with their parent scope so that name resolution works properly throughout the compilation process.

### Additional context

This might be related to the order of operations during AST node parsing. The scope assignment for function identifiers seems to be happening at the wrong time or referencing the wrong scope object.

---
Repository: /testbed
