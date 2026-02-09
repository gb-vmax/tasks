# Bug Report

### Describe the bug

There seems to be a syntax error in the Swagger 2 importer that's preventing the application from running. The code appears to have malformed structure in the `generateParameterExample` function where the `number_double` generator is defined.

### Reproduction

When trying to import a Swagger 2.0 specification with number/double type parameters, the importer fails to load properly. This affects any API specification that includes numeric parameters with double precision.

Steps to reproduce:
1. Try to import any Swagger 2.0 spec file
2. The importer module fails to initialize
3. Application becomes unusable for Swagger 2 imports

### Expected behavior

The Swagger 2 importer should load without errors and be able to process specifications with double-precision numeric parameters correctly.

### Additional context

This appears to be affecting the parameter example generation logic. The issue is blocking any Swagger 2.0 imports from working at all since the module can't be loaded.

---
Repository: /testbed
