# Bug Report

### Describe the bug

After a recent update, the API spec parser is throwing syntax errors when trying to load OpenAPI specifications. The application fails to start and shows compilation errors related to the `resolveComponentSchemaRefs` function in `api-specs.ts`.

### Reproduction

1. Start the application with any OpenAPI spec file
2. The app crashes during the parsing phase
3. Console shows duplicate function declarations and syntax errors

It looks like there might be some duplicate code or malformed function definitions in the schema resolution logic. The error prevents the entire application from loading properly.

### Expected behavior

The API spec parser should successfully parse OpenAPI specifications and resolve component schema references without throwing syntax errors. The application should start normally.

### System Info
- Insomnia version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
