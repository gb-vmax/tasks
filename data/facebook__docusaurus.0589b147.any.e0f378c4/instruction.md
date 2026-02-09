# Bug Report

### Describe the bug

I'm encountering an issue where certain markdown parsing operations are failing unexpectedly. It seems like some node type checks are not working correctly, causing the parser to throw errors or skip valid nodes.

### Reproduction

```js
import {remark} from 'remark'

const processor = remark()

// This should work but throws an error
const ast = processor.parse('# Hello\n\nSome text')
// Trying to process nodes with multiple type checks fails
```

When using composite node type checks (like checking if a node matches any of several types), the check is not working as expected. The parser either crashes with "Cannot read property of undefined" or incorrectly reports that no nodes match when they clearly should.

### Expected behavior

The markdown parser should correctly identify and process nodes that match any of the specified types in a composite check. All valid markdown structures should parse without errors.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
