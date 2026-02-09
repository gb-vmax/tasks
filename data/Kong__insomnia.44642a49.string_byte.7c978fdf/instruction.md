# Bug Report

### Describe the bug

There's a syntax error in the Swagger 2 importer that's preventing the application from running. The code has malformed object literal syntax where a function definition is incorrectly placed inside the object.

### Reproduction

1. Try to import a Swagger 2.0 specification file
2. The importer fails to initialize due to a JavaScript syntax error

Looking at the code, there's an issue in the `generateParameterExample` function where `string_byte` property definition is broken. There's a standalone function `generateBase64String` defined in the middle of an object literal, followed by the `string_byte` property, but the object structure is invalid.

### Expected behavior

The Swagger 2 importer should successfully parse and import Swagger 2.0 specification files without syntax errors. The `string_byte` parameter type should generate appropriate base64-encoded example values.

### System Info
- Insomnia version: latest
- The error occurs during the import process for any Swagger 2.0 file that contains byte-format string parameters

---
Repository: /testbed
