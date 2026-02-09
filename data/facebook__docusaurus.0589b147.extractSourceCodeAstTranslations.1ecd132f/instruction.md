# Bug Report

### Describe the bug

I'm experiencing an issue with the translation extraction where components with only whitespace/newline content are being incorrectly filtered out. The filter logic seems to be inverted, causing translations with actual content to be excluded while empty ones are kept.

### Reproduction

```jsx
import Translate from '@docusaurus/Translate';

// This translation gets filtered out incorrectly
<Translate id="hello">
  Hello World
</Translate>

// Empty translations with just newlines/spaces might be kept instead
<Translate id="empty">
  
</Translate>
```

When running the translation extraction, translations with actual text content are being removed from the extraction results, while empty/whitespace-only translations may be processed.

### Expected behavior

The translation extractor should:
1. Filter out JSX text nodes that contain only whitespace/newlines
2. Keep and process text nodes that have actual content
3. Properly extract the message from non-empty translation components

Currently it seems to be doing the opposite - keeping empty nodes and filtering out the ones with content.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

---
Repository: /testbed
