Hey, I need your help packaging my web project for deployment. I have a project directory at `/home/user/webproject` that contains several files, but I only want to bundle the production assets — not the development config or the node_modules-style junk.

Here's what I need you to do:

1. Create a gzip-compressed tar archive called `deploy.tar.gz` in `/home/user` that contains only these specific files from `/home/user/webproject`:
   - `index.html`
   - `style.css`
   - `app.js`

   Do NOT include `dev.config.json` or `notes.txt` in the archive. The files should be archived with their paths relative to `/home/user/webproject` (i.e., they should appear as `index.html`, `style.css`, and `app.js` inside the archive — no leading `/home/user/webproject/` prefix).

2. Verify the archive contents by listing them and saving the output to `/home/user/archive_contents.txt`. The file should contain exactly the output of running `tar -tzf /home/user/deploy.tar.gz`, one filename per line, with no extra text.

3. Extract the archive into a new directory `/home/user/deployment/` so that the three files are accessible at `/home/user/deployment/index.html`, `/home/user/deployment/style.css`, and `/home/user/deployment/app.js`.

Can you handle all of this for me?
