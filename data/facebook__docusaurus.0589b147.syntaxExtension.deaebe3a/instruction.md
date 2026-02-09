# Bug Report

### Describe the bug

I'm experiencing an issue with syntax extensions not being properly registered. When I try to use custom syntax extensions, they don't seem to work at all - the parser just ignores them completely.

### Reproduction

```js
const unified = require('unified');
const remarkParse = require('remark-parse');

const processor = unified()
  .use(remarkParse)
  .use(() => {
    const data = this.data();
    
    // Try to add a custom syntax extension
    const micromarkExtensions = data.micromarkExtensions || (data.micromarkExtensions = []);
    micromarkExtensions.push({
      text: {
        91: { // '[' character
          tokenize: myCustomTokenizer
        }
      }
    });
  });

const result = processor.parse('[custom syntax]');
// Custom syntax is not recognized, parsed as regular text instead
```

### Expected behavior

The custom syntax extension should be registered and used during parsing. The parser should recognize and tokenize the custom syntax patterns according to the extension definition.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems like a regression as similar code worked in previous versions. The extensions are being added but not actually applied during parsing.

---
Repository: /testbed
