# Bug Report

### Describe the bug

I'm experiencing an issue with strikethrough parsing in remark-gfm where strikethrough syntax is not being recognized correctly. When I use double tildes (`~~`) to mark text as strikethrough, it's not working as expected in certain cases.

### Reproduction

```js
const text = "This is ~~strikethrough~~ text";
// Parse with remark-gfm
const result = parse(text);
// Strikethrough is not being detected properly
```

I've noticed this particularly happens when there are multiple strikethrough sections in the same document. Sometimes the first one works but subsequent ones don't get parsed correctly.

### Expected behavior

All text wrapped in double tildes (`~~text~~`) should be parsed as strikethrough and rendered appropriately. The parser should correctly match opening and closing strikethrough sequences regardless of their position in the document.

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

Any help would be appreciated! This is blocking our markdown rendering pipeline.

---
Repository: /testbed
