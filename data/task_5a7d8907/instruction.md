I'm a localization engineer maintaining a translations system for a multi-language web application. The project lives at `/home/user/l10n`. Inside this directory there are two subdirectories:

- `/home/user/l10n/versions/` — contains the actual versioned translation `.po` files (the source of truth)
- `/home/user/l10n/active/` — contains symbolic links that point into `versions/`, representing the currently active translation for each locale

Something has gone wrong — some of the symlinks in `active/` are pointing to old file versions, one symlink is completely broken (its target no longer exists), and two new locales need to be set up. I also need a manifest file generated at the end.

Here's what I need you to do:

**1. Fix the broken symlink**

Inside `/home/user/l10n/active/`, the symlink `pt_BR.po` is broken — its target file no longer exists. It should instead point to `/home/user/l10n/versions/pt_BR_v2.po`. Remove the old broken symlink and create a new one in its place.

**2. Update the stale symlink**

The symlink `fr.po` in `active/` currently points to `../versions/fr_v1.po`. It needs to be updated to point to `../versions/fr_v2.po` instead. Use a relative symlink target (not an absolute path). Remove the old symlink and create the corrected one.

**3. Create symlinks for two new locales**

Create the following new symlinks in `/home/user/l10n/active/`, both using relative targets:
- `ja.po` → `../versions/ja_v1.po`
- `ko.po` → `../versions/ko_v1.po`

**4. Generate the manifest**

After all symlinks are in place, generate a manifest file at `/home/user/l10n/active/MANIFEST.txt`. This file must list every symlink in the `active/` directory (and only symlinks — not the manifest file itself or any regular files), one per line, in **alphabetical order by symlink name**. Each line must follow this exact format:

```
<symlink_name> -> <symlink_target>
```

Where `<symlink_target>` is exactly what `readlink` reports for that symlink (the literal stored target, not the resolved absolute path). There must be a single space on each side of the `->` arrow. No trailing spaces. The file must end with a newline after the last entry.

For example, a line might look like:
```
de.po -> ../versions/de_v3.po
```

The manifest should contain exactly 5 entries (one per locale: `de.po`, `es.po`, `fr.po`, `ja.po`, `ko.po`, `pt_BR.po` — wait, that's 6. Let me be precise: the active directory will contain symlinks for `de.po`, `es.po`, `fr.po`, `ja.po`, `ko.po`, and `pt_BR.po` — exactly 6 symlinks — so the manifest must have exactly 6 lines).

Do not include the `MANIFEST.txt` file itself in the manifest output. The manifest file is a regular file, not a symlink, so it should naturally be excluded if you only enumerate symlinks.
