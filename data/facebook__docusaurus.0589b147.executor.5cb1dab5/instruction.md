# Bug Report

### Describe the bug

I'm encountering an issue with the remark processor where processing markdown appears to be failing silently. When I try to process markdown content, the processor doesn't seem to be handling errors correctly and I'm getting unexpected behavior with the output.

### Reproduction

```js
import {remark} from 'remark'

const processor = remark()

// Try processing some markdown
processor.process('# Hello World', (err, file) => {
  if (err) {
    console.error('Error:', err)
  } else {
    console.log('Result:', file)
  }
})
```

### Expected behavior

The processor should either successfully process the markdown and return the result, or properly propagate any errors that occur during processing. Currently it seems like errors aren't being handled correctly and the callback receives unexpected values.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
