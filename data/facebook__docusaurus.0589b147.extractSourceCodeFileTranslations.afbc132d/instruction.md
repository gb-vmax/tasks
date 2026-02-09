# Bug Report

### Describe the bug

Translation extraction is silently failing for source code files with syntax errors. When there's an error parsing a file (e.g., invalid JavaScript/TypeScript syntax), the extraction process returns an empty translations object instead of propagating the error. This makes it very difficult to debug translation issues since errors are logged but don't cause the build to fail.

### Reproduction

Create a source code file with invalid syntax that contains translation calls:

```js
// invalid-file.js
import Translate from '@docusaurus/Translate';

// Missing closing brace - syntax error
function MyComponent() {
  return (
    <Translate id="my.translation">
      Hello World
    </Translate>
  
}
```

When running the translation extraction, the error is logged but the process continues and returns an empty object. The translations from this file are silently lost, and there's no indication in the build output that something went wrong beyond a logged error message.

### Expected behavior

The extraction should fail loudly when encountering parse errors so developers are aware that translations are missing. Silent failures make it hard to track down why certain translations aren't being extracted.

### Additional context

This seems to affect any file with syntax errors during the Babel parsing phase. The error gets caught and logged, but then an empty translations object is returned instead of re-throwing the error.

---
Repository: /testbed
