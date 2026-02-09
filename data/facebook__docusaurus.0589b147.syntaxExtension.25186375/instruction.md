# Bug Report

### Describe the bug

I'm experiencing an issue with syntax extension handling in the remark parser. When registering custom syntax extensions with hooks, the extensions are not being properly merged or applied. It seems like the hook handlers are not being registered correctly, causing custom syntax to be ignored.

### Reproduction

```js
const unified = require('unified')
const remarkParse = require('remark-parse')

// Define a custom syntax extension
const customExtension = {
  tokenize: function(effects, ok, nok) {
    // custom tokenizer logic
  }
}

const processor = unified()
  .use(remarkParse)
  .use(function() {
    const data = this.data()
    const micromarkExtensions = data.micromarkExtensions || (data.micromarkExtensions = [])
    
    micromarkExtensions.push({
      text: {
        91: customExtension  // code 91 for '['
      }
    })
  })

// Try to parse text with custom syntax
const result = processor.processSync('some [custom] syntax')

// Custom syntax is not recognized/processed
console.log(result)
```

### Expected behavior

The custom syntax extension should be properly registered and applied during parsing. The tokenizer should be called when the specified character code is encountered in the input text.

### System Info
- remark version: 15.0.1
- Node.js: v18.x

The extensions worked fine in previous versions but seem to have broken recently. Any help would be appreciated!

---
Repository: /testbed
