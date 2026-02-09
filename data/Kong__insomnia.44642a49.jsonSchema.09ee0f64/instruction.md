# Bug Report

### Describe the bug

When using `expect(response).to.have.jsonSchema()` in test scripts, the assertion is not working as expected. The schema validation appears to be passing when it should fail, or the behavior has changed from previous versions.

### Reproduction

```js
pm.test("Response should match JSON schema", function () {
    const schema = {
        type: "object",
        properties: {
            id: { type: "number" },
            name: { type: "string" }
        },
        required: ["id", "name"]
    };
    
    // This assertion behaves unexpectedly
    pm.expect(pm.response).to.have.jsonSchema(schema);
});
```

### Expected behavior

The `jsonSchema` assertion should properly validate the response body against the provided schema and fail when the response doesn't match the schema structure.

### System Info
- Insomnia SDK version: latest
- Environment: Request scripts

---
Repository: /testbed
