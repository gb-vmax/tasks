# Bug Report

### Describe the bug

The application fails to start after a recent update. I'm getting syntax errors when trying to load the plugins module. It looks like there's something wrong with the DocumentAction interface definition - the code structure seems completely broken.

### Reproduction

1. Start the application
2. Application crashes immediately with a syntax/parsing error
3. Error points to the plugins/index.ts file around the DocumentAction interface

### Expected behavior

The application should start normally without any syntax errors. The DocumentAction interface should be properly defined with its `action` and `label` properties.

### Additional context

This appears to have broken after a recent commit. The DocumentAction interface seems to have been corrupted - there's a function definition (`flattenSchemaReferences`) that's somehow inserted into the middle of the interface definition, which is clearly invalid TypeScript syntax.

The interface should define the structure for document actions, not contain function implementations.

---
Repository: /testbed
