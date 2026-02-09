# Bug Report

### Describe the bug

I'm experiencing an issue with remark parsing where the markdown extensions are not being applied correctly. It seems like the parser is confusing which extensions go where - micromark extensions and mdast extensions appear to be swapped.

### Reproduction

```js
const unified = require('unified');
const remarkParse = require('remark-parse');

const processor = unified()
  .use(remarkParse)
  .data('micromarkExtensions', [myMicromarkExtension])
  .data('fromMarkdownExtensions', [myMdastExtension]);

const result = processor.parse('# Hello');
// Extensions are not applied as expected
```

When I configure my processor with micromark extensions and mdast extensions through the `data()` API, the parser doesn't process the markdown correctly. The extensions seem to be ignored or applied to the wrong stage of parsing.

### Expected behavior

The parser should correctly apply:
- `micromarkExtensions` to the micromark tokenization phase
- `fromMarkdownExtensions` to the mdast tree building phase

The markdown should be parsed with the custom extensions working as intended.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
