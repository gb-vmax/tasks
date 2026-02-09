# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where custom extensions aren't being applied correctly. When I register mdast extensions using `data("fromMarkdownExtensions")`, they don't seem to be picked up by the parser.

### Reproduction

```js
const processor = remark()
  .data('fromMarkdownExtensions', [myCustomExtension])
  .use(somePlugin);

const result = processor.processSync(markdownContent);
// Custom extension transformations are not applied
```

### Expected behavior

The parser should use the mdast extensions registered via `data("fromMarkdownExtensions")` to transform the markdown AST. Instead, it appears to be looking for extensions in the wrong data key.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have broken after a recent update. The extensions work fine when passed directly as options, but not when set through the data API.

---
Repository: /testbed
