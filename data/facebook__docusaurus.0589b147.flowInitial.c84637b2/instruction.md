# Bug Report

### Describe the bug

I'm encountering an issue where the `flowInitial` construct appears to be missing from the exported constructs in the remark vendor file. This is causing errors when trying to parse markdown content that relies on initial flow content detection.

### Reproduction

```js
import {constructs} from './vendor/remark@15.0.1.js';

// Trying to access flowInitial
console.log(constructs.flowInitial);
// Returns: undefined

// This causes parsing to fail for documents starting with flow content
const parser = createParser();
parser.parse('# Heading\n\nParagraph text');
// Error: Cannot read property of undefined
```

### Expected behavior

The `flowInitial` construct should be exported and accessible from the constructs object, allowing proper parsing of markdown documents that begin with flow-level content like headings, paragraphs, lists, etc.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have broken markdown parsing for documents that don't start with inline content. Any help would be appreciated!

---
Repository: /testbed
