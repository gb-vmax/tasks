# Bug Report

### Describe the bug

I'm experiencing an issue with the response assertions in the SDK. When trying to use `expect(response).to.have.jsonBody()`, the assertion is failing even though the response body contains the expected JSON structure.

### Reproduction

```js
const response = {
  body: JSON.stringify({
    id: 123,
    name: 'test',
    metadata: {
      created: '2024-01-01'
    }
  })
}

// This assertion fails unexpectedly
expect(response).to.have.jsonBody({
  id: 123,
  name: 'test'
})
```

### Expected behavior

The assertion should pass when the response body contains the expected JSON properties. It seems like the matcher is too strict and requires an exact match instead of checking if the expected properties are present in the response.

### Additional context

This used to work in previous versions where we could check for partial matches in JSON responses. Now it appears the behavior has changed and I'm not sure if this is intentional or a regression.

---
Repository: /testbed
