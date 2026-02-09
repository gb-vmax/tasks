# Bug Report

### Describe the bug

The `response.to.not.have.jsonSchema()` assertion is not working correctly. When I try to assert that a response does NOT match a JSON schema, the behavior seems inverted - it's checking if the response matches the schema instead of checking that it doesn't match.

### Reproduction

```js
// This should pass but fails
pm.test("Response should not match schema", function() {
    const schema = {
        type: "object",
        properties: {
            name: { type: "string" }
        }
    };
    
    // Response body: { "age": 25 }
    pm.response.to.not.have.jsonSchema(schema);
});

// This should fail but passes
pm.test("Response should not match schema", function() {
    const schema = {
        type: "object",
        properties: {
            age: { type: "number" }
        }
    };
    
    // Response body: { "age": 25 }
    pm.response.to.not.have.jsonSchema(schema);
});
```

### Expected behavior

When using `response.to.not.have.jsonSchema()`, it should pass when the response body does NOT match the provided schema, and fail when it does match. Currently it seems to be doing the opposite.

The positive assertion `response.to.have.jsonSchema()` works fine, it's only the negated version that has this issue.

---
Repository: /testbed
