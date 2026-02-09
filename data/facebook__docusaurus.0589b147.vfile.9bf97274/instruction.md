# Bug Report

### Describe the bug

I'm experiencing an issue with file processing where the content of files is being lost or not properly handled. When passing file data through the processing pipeline, the output comes back empty or undefined instead of containing the expected content.

### Reproduction

```js
const processor = remark();
const fileContent = 'some markdown content';

// Process the file content
const result = processor.processSync(fileContent);

// Result is empty or doesn't contain the expected content
console.log(result.value); // Expected: processed markdown, Actual: undefined or empty
```

### Expected behavior

When passing a string or file content to the processor, it should properly process the content and return the result with the processed value. The file content should be preserved and transformed, not lost during processing.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
