import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(ROOT, "docs")
TEMPLATES_DIR = os.path.join(ROOT, "templates")

NAV_FILE = os.path.join(TEMPLATES_DIR, "nav.html")
FOOTER_FILE = os.path.join(TEMPLATES_DIR, "footer.html")
CSS_FILE = os.path.join(TEMPLATES_DIR, "extra.css")

CSS_START = "/* KDCN V1.1 COMPONENTS START */"
CSS_END = "/* KDCN V1.1 COMPONENTS END */"

# ---------------------------------------------------------
# Read master components
# ---------------------------------------------------------

with open(NAV_FILE, "r", encoding="utf-8") as f:
    nav_html = f.read().strip()

with open(FOOTER_FILE, "r", encoding="utf-8") as f:
    footer_html = f.read().strip()

with open(CSS_FILE, "r", encoding="utf-8") as f:
    extra_css = f.read().strip()


# ---------------------------------------------------------
# Add controlled CSS markers
# ---------------------------------------------------------

if CSS_START not in extra_css:
    extra_css = (
        CSS_START
        + "\n"
        + extra_css
        + "\n"
        + CSS_END
    )


# ---------------------------------------------------------
# Process every HTML page
# ---------------------------------------------------------

updated = 0

for filename in sorted(os.listdir(DOCS_DIR)):

    if not filename.endswith(".html"):
        continue

    filepath = os.path.join(DOCS_DIR, filename)

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()


    # -----------------------------------------------------
    # Replace navigation
    # -----------------------------------------------------

    if re.search(r"<nav\b.*?</nav>", content, flags=re.DOTALL | re.IGNORECASE):
        content = re.sub(
            r"<nav\b.*?</nav>",
            nav_html,
            content,
            count=1,
            flags=re.DOTALL | re.IGNORECASE
        )
    else:
        content = content.replace(
            "<body>",
            "<body>\n" + nav_html,
            1
        )


    # -----------------------------------------------------
    # Replace footer
    # -----------------------------------------------------

    if re.search(r"<footer\b.*?</footer>", content, flags=re.DOTALL | re.IGNORECASE):
        content = re.sub(
            r"<footer\b.*?</footer>",
            footer_html,
            content,
            count=1,
            flags=re.DOTALL | re.IGNORECASE
        )
    else:
        content = content.replace(
            "</body>",
            footer_html + "\n</body>",
            1
        )


    # -----------------------------------------------------
    # Remove ALL previous V1.1 CSS injections
    #
    # This also removes the older:
    # "KDCN new navigation CTA button"
    # injection created by the previous script.
    # -----------------------------------------------------

    content = re.sub(
        r"/\* KDCN V1\.1 COMPONENTS START \*/.*?/\* KDCN V1\.1 COMPONENTS END \*/\s*",
        "",
        content,
        flags=re.DOTALL
    )

    content = re.sub(
        r"/\* KDCN new navigation CTA button \*/.*?(?=</style>)",
        "",
        content,
        flags=re.DOTALL
    )


    # -----------------------------------------------------
    # Inject exactly ONE clean V1.1 component block
    # -----------------------------------------------------

    if "</style>" in content:

        content = content.replace(
            "</style>",
            "\n" + extra_css + "\n</style>",
            1
        )

    else:

        head_match = re.search(
            r"</head>",
            content,
            flags=re.IGNORECASE
        )

        if head_match:
            content = content.replace(
                "</head>",
                "<style>\n" + extra_css + "\n</style>\n</head>",
                1
            )


    # -----------------------------------------------------
    # Write page
    # -----------------------------------------------------

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    updated += 1
    print(f"[UPDATED] {filename}")


print()
print("=" * 60)
print("KDCN WEBSITE V1.1 UPDATE COMPLETE")
print("=" * 60)
print(f"Pages updated: {updated}")
print("Navigation:        V1.1")
print("Footer:            V1.1")
print("Component CSS:     ONE controlled block per page")
print("Social floating:   controlled by page/chat implementation")
print("Backup:            docs.backup-v1.1")
print("=" * 60)
