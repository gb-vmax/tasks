# Bug Report

### Describe the bug

I'm encountering an issue with MDX import statements parsing. When I have an import statement with just a source (no specifiers), the parser seems to be handling it incorrectly. The semicolon appears to be consumed at the wrong point in the parsing flow.

### Reproduction

```mdx
import 'some-module';

export default function Component() {
  return <div>Content</div>
}
```

When parsing this type of import statement (without any specifiers, just importing a module for side effects), the parser behavior seems off. The import source isn't being captured correctly.

### Expected behavior

Import statements without specifiers (side-effect imports) should be parsed correctly, with the source being properly extracted and the statement being recognized as valid.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
