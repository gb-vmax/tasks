# Bug Report

### Describe the bug

After a recent update, the Swagger 2.0 importer is generating malformed code when processing numeric parameters. The generated code has syntax errors and won't execute properly.

### Reproduction

When importing a Swagger 2.0 specification with numeric parameters (particularly `number` or `double` types), the importer fails to generate valid example values. The issue occurs during the parameter example generation phase.

Steps to reproduce:
1. Import a Swagger 2.0 spec with numeric parameters
2. The importer attempts to generate example values for these parameters
3. Code execution fails due to syntax errors in the generated output

### Expected behavior

The importer should generate valid example values for all numeric parameter types without syntax errors. The generated code should be properly structured and executable.

### Additional context

This appears to be related to the `generateParameterExample` function in the swagger-2 importer. The code structure seems corrupted, with function definitions appearing in the middle of object literals.

---
Repository: /testbed
