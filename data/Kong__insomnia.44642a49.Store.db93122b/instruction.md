# Bug Report

### Describe the bug
After a recent update, I'm encountering a syntax error in the sync store module. The application fails to start with a compilation error indicating there's a duplicate class declaration.

### Reproduction
When trying to initialize the application, I get the following error:

```
SyntaxError: Identifier 'Store' has already been declared
```

Looking at the store implementation, it appears that the `Store` class is defined twice in the same file, which causes the JavaScript/TypeScript parser to fail.

### Expected behavior
The application should compile and start successfully without syntax errors. The Store class should be defined only once with all its methods and properties properly contained within a single class declaration.

### System Info
- Node version: 18.x
- TypeScript version: 5.x

This is blocking our ability to use the sync functionality at all since the module won't even load.

---
Repository: /testbed
