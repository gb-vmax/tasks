# Bug Report

### Describe the bug

I'm experiencing an issue with syntax extensions in remark. When trying to register custom syntax extensions, they don't seem to be applied correctly. The parser is not recognizing the custom syntax patterns I've defined, and the extensions appear to be completely ignored.

### Reproduction

```js
import {remark} from 'remark'

const processor = remark()
  .use(() => {
    const data = this.data()
    
    const micromarkExtensions = data.micromarkExtensions || (data.micromarkExtensions = [])
    micromarkExtensions.push({
      text: {
        91: {  // Custom syntax for '['
          tokenize: function(effects, ok, nok) {
            // ... tokenizer implementation
          }
        }
      }
    })
  })

const result = processor.processSync('[custom syntax]')
console.log(result)
```

Expected: The custom syntax should be parsed and transformed according to the extension
Actual: The extension is completely ignored and the text is parsed as regular markdown

### Additional context

This seems to affect all types of syntax extensions (text, flow, string, etc.). The hooks are registered but never actually get invoked during parsing. I've verified that the extension object is being passed correctly, but something in the registration logic appears broken.

This is blocking our ability to add custom markdown syntax to our documentation system.

---
Repository: /testbed
