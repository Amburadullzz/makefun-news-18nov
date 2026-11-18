// Entry program for make.fun news-image-20261118 (Node 22, standard library only).
//
// It copies the image that sits beside this file, entry.png, into the grader's
// output directory: $MAKEFUN_OUTPUT_DIR when that variable is set, otherwise
// /output. The destination directory is created if it does not exist yet. The
// bytes are copied verbatim, so the judge sees exactly the PNG committed here.
//
// Local run, mirroring the grader:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const source = fileURLToPath(new URL("./entry.png", import.meta.url));
const outputDir = process.env.MAKEFUN_OUTPUT_DIR || "/output";
const destination = join(outputDir, "entry.png");

mkdirSync(outputDir, { recursive: true });
copyFileSync(source, destination);

console.log(`copied ${source} -> ${destination}`);
