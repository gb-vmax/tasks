# Bug Report

### Describe the bug

There's a syntax error in the response.ts file that's preventing the code from compiling. It looks like some utility functions for JSON path extraction and partial matching were added in the middle of an object definition, breaking the object structure.

### Reproduction

When trying to use the SDK after the recent changes, the code fails to compile/run because of a malformed object literal in the response expectations.

```js
// Attempting to use response expectations
pm.expect(response).to.have.jsonBody({ ... });
```

This results in a syntax error because the object definition is incomplete.

### Expected behavior

The code should compile successfully and the response object expectations should work as intended. The object literal containing the `not` property and its nested expectations should be properly closed before any helper functions are defined.

### Additional context

The issue appears to be in the `packages/insomnia-sdk/src/objects/response.ts` file around line 258. Several utility functions (`isPartialMatchIndicator`, `extractJsonPath`, `partialMatchObject`) seem to have been inserted directly into the middle of an object definition, causing the syntax to break.

---
Repository: /testbed
