# Bug Report

### Describe the bug

When importing Postman collections with empty raw body content (containing only whitespace), the importer crashes instead of handling it gracefully. The application throws an error when trying to process requests that have bodies with whitespace-only strings.

### Reproduction

```js
// Import a Postman collection with a request that has:
{
  body: {
    mode: 'raw',
    raw: '   ' // whitespace only
  }
}
```

Steps to reproduce:
1. Create a Postman collection with a request
2. Set the request body to raw mode
3. Add only whitespace characters (spaces, tabs, newlines) to the raw body field
4. Try to import the collection into Insomnia

### Expected behavior

The importer should handle empty/whitespace-only raw body content without crashing. It should either treat it as an empty body or skip it gracefully.

### Actual behavior

The application throws an error because it's trying to call `.trim()` on a value that might be undefined or null.

---
Repository: /testbed
