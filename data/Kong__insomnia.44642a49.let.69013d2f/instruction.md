# Bug Report

### Describe the bug

When generating HAR files with file attachments, the function `getRequestPostData` has a syntax error that breaks the entire code generation process. The function declaration appears twice in the code, causing a parsing error.

### Reproduction

```js
// Try to generate HAR data for a request with a file attachment
const renderedRequest = {
  body: {
    fileName: '/path/to/file.json',
    mimeType: 'application/json'
  }
};

const postData = getRequestPostData(renderedRequest);
// This will fail to execute due to duplicate function declaration
```

### Expected behavior

The function should execute without syntax errors and properly read the file, detect its MIME type, and return the post data object.

### Additional context

This seems to have been introduced in a recent change that added MIME type detection and file size validation. The code has a nested function declaration which is causing issues when trying to use the HAR export functionality.

---
Repository: /testbed
