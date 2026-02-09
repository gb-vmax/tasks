# Bug Report

### Describe the bug

When using `response.to.have.jsonSchema()` in test scripts, the validation is not working properly. It seems like the function signature was changed but the implementation doesn't match, causing the schema validation to fail silently or throw unexpected errors.

### Reproduction

```js
pm.test("Response matches schema", function () {
    const schema = {
        type: "object",
        properties: {
            id: { type: "number" },
            name: { type: "string" }
        },
        required: ["id", "name"]
    };
    
    pm.response.to.have.jsonSchema(schema);
});
```

When running this test, the schema validation doesn't work as expected. The issue appears to be related to how the jsonSchema assertion is being processed.

### Expected behavior

The response should be validated against the provided JSON schema, and any validation errors should be reported clearly. The assertion should support both simple schema objects and objects with additional AJV options like `{ schema: {...}, ajvOptions: {...} }`.

### System Info

- Insomnia SDK version: latest
- Environment: Pre-request/Test scripts

---
Repository: /testbed
