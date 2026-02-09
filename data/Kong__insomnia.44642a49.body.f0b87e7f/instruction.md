# Bug Report

### Describe the bug

After a recent update, the response body assertion is behaving incorrectly. When checking if a response body contains or equals a specific string, the assertion passes even when it shouldn't.

### Reproduction

```js
// This should fail but passes
response.to.not.have.body('some text')
// Even when the response body actually contains 'some text'

// Similar issue with regex patterns
response.to.not.have.body(/pattern/)
// Passes even when the body matches the pattern
```

### Expected behavior

When using `response.to.not.have.body()`, the assertion should fail if the body contains or matches the expected value. Currently it seems like the negation logic is inverted - assertions that should fail are passing.

### Additional context

This seems to have started after the latest changes to the response object. The `have.body()` assertions with negation (`not.have.body`) are not working as expected. Both string matching and regex pattern matching are affected.

---
Repository: /testbed
