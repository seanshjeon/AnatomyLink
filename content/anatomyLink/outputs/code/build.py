#!/usr/bin/env python3
"""
Build AnatomyLink HTML site from Obsidian vault
"""

import os
import json
from pathlib import Path
from converter import MarkdownToHTMLConverter

# Configuration
VAULT_PATH = Path('/sessions/exciting-adoring-gates/mnt/anatomyLink')
OUTPUT_PATH = Path('/sessions/exciting-adoring-gates/mnt/outputs/html_output')
ASSETS_PATH = Path('/sessions/exciting-adoring-gates/mnt/outputs/code')

class AnatomyLinkBuilder:
    def __init__(self, vault_path, output_path):
        self.vault_path = Path(vault_path)
        self.output_path = Path(output_path)
        self.file_index = {}  # Maps file titles to relative paths
        self.pages_data = {}  # Stores page metadata

    def scan_vault(self):
        """Scan vault and build file index"""
        print("🔍 Scanning vault...")

        for md_file in self.vault_path.rglob('*.md'):
            # Get file title from filename
            title = md_file.stem

            # Calculate relative path from vault root
            rel_path = md_file.relative_to(self.vault_path)
            rel_path_str = str(rel_path).replace('\\', '/')

            self.file_index[title] = rel_path_str

            # Also index by file path without .md
            self.file_index[rel_path_str.replace('.md', '')] = rel_path_str

        print(f"✅ Found {len(self.file_index)} files")
        return self.file_index

    def build_site(self):
        """Build the entire HTML site"""
        print("\n🏗️  Building HTML site...")

        # Create output directory
        self.output_path.mkdir(parents=True, exist_ok=True)

        # Initialize converter
        converter = MarkdownToHTMLConverter(self.file_index)

        # Process each markdown file
        md_files = list(self.vault_path.rglob('*.md'))
        print(f"📄 Processing {len(md_files)} markdown files...")

        for i, md_file in enumerate(md_files, 1):
            print(f"  [{i}/{len(md_files)}] {md_file.name}...", end='', flush=True)

            # Create output directory structure
            rel_path = md_file.relative_to(self.vault_path)
            output_file = self.output_path / rel_path.with_suffix('.html')
            output_file.parent.mkdir(parents=True, exist_ok=True)

            # Read and convert markdown
            with open(md_file, 'r', encoding='utf-8') as f:
                markdown_content = f.read()

            # Convert to HTML
            content_html = converter.convert_markdown_to_html(markdown_content)

            # Generate full HTML page
            html_page = self.generate_html_page(md_file.stem, content_html, md_file)

            # Write HTML file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_page)

            print(" ✓")

        # Create index page
        self.create_index_page(converter)

        # Copy CSS
        self.copy_css()

        print(f"\n✅ Site built successfully!")
        print(f"📁 Output: {self.output_path}")

    def generate_html_page(self, title, content, md_file):
        """Generate a complete HTML page"""
        rel_path = md_file.relative_to(self.vault_path)
        breadcrumbs = self.generate_breadcrumbs(rel_path)

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - AnatomyLink</title>
    <link rel="stylesheet" href="{'../' * (len(rel_path.parts) - 1)}styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <a href="{'../' * (len(rel_path.parts) - 1)}index.html" class="nav-home">🫀 AnatomyLink</a>
            <div class="nav-search">
                <input type="search" id="search-box" placeholder="Search...">
            </div>
        </div>
    </nav>

    <div class="breadcrumbs">
        {breadcrumbs}
    </div>

    <div class="container">
        <main class="content">
            {content}
        </main>

        <aside class="sidebar">
            <div class="sidebar-section">
                <h3>📚 Systems</h3>
                <ul>
                    <li><a href="{'../' * (len(rel_path.parts) - 1)}Skeletal%20System.html">🦴 Skeletal</a></li>
                    <li><a href="{'../' * (len(rel_path.parts) - 1)}Muscular%20System.html">💪 Muscular</a></li>
                    <li><a href="{'../' * (len(rel_path.parts) - 1)}Nervous%20System.html">🧠 Nervous</a></li>
                    <li><a href="{'../' * (len(rel_path.parts) - 1)}Circulatory%20System.html">🫀 Circulatory</a></li>
                    <li><a href="{'../' * (len(rel_path.parts) - 1)}Digestive%20System.html">🫁 Digestive</a></li>
                </ul>
            </div>
        </aside>
    </div>

    <footer>
        <p>AnatomyLink © 2026 | Learning resource for medical students</p>
    </footer>

    <script src="{'../' * (len(rel_path.parts) - 1)}script.js"></script>
</body>
</html>
"""

    def generate_breadcrumbs(self, rel_path):
        """Generate breadcrumb navigation"""
        parts = rel_path.parts[:-1]  # Exclude filename
        breadcrumbs = ['<a href="index.html">Home</a>']

        for i, part in enumerate(parts):
            url = '/'.join(parts[:i+1]).replace(' ', '%20') + '.html'
            breadcrumbs.append(f'<a href="{url}">{part}</a>')

        breadcrumbs.append(f'<span>{rel_path.stem}</span>')

        return ' / '.join(breadcrumbs)

    def create_index_page(self, converter):
        """Create index page"""
        print("\n📄 Creating index page...")

        # Read home page
        home_file = self.vault_path / '00 - AnatomyLink Home.md'
        with open(home_file, 'r', encoding='utf-8') as f:
            home_content = f.read()

        content_html = converter.convert_markdown_to_html(home_content)

        html_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AnatomyLink - Human Anatomy Navigator</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <a href="index.html" class="nav-home">🫀 AnatomyLink</a>
            <div class="nav-search">
                <input type="search" id="search-box" placeholder="Search...">
            </div>
        </div>
    </nav>

    <div class="container">
        <main class="content index-page">
            {content_html}
        </main>

        <aside class="sidebar">
            <div class="sidebar-section">
                <h3>📚 Main Systems</h3>
                <ul>
                    <li><a href="Skeletal%20System.html">🦴 Skeletal System</a></li>
                    <li><a href="Muscular%20System.html">💪 Muscular System</a></li>
                    <li><a href="Nervous%20System.html">🧠 Nervous System</a></li>
                    <li><a href="Circulatory%20System.html">🫀 Circulatory System</a></li>
                    <li><a href="Digestive%20System.html">🫁 Digestive System</a></li>
                    <li><a href="Ligament%20System.html">🔗 Ligament System</a></li>
                </ul>
            </div>

            <div class="sidebar-section">
                <h3>🎓 About</h3>
                <p>AnatomyLink is an interactive learning resource designed for medical and anatomy students. Navigate through interconnected anatomical structures to understand how they relate to each other.</p>
            </div>
        </aside>
    </div>

    <footer>
        <p>AnatomyLink © 2026 | Interactive anatomy learning platform</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
"""

        output_file = self.output_path / 'index.html'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_page)

    def copy_css(self):
        """Create CSS file"""
        print("🎨 Creating stylesheets...")

        css_content = """/* AnatomyLink Stylesheet */

:root {
    --primary-color: #2c3e50;
    --secondary-color: #e74c3c;
    --accent-color: #3498db;
    --light-bg: #ecf0f1;
    --border-color: #bdc3c7;
    --text-color: #2c3e50;
    --link-color: #e74c3c;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html, body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f8f9fa;
    color: var(--text-color);
    line-height: 1.6;
}

/* Navigation */
.navbar {
    background-color: var(--primary-color);
    color: white;
    padding: 1rem 0;
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.nav-home {
    font-size: 1.5rem;
    font-weight: bold;
    color: white;
    text-decoration: none;
    transition: opacity 0.3s;
}

.nav-home:hover {
    opacity: 0.8;
}

.nav-search input {
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 4px;
    min-width: 250px;
}

/* Breadcrumbs */
.breadcrumbs {
    background-color: white;
    padding: 1rem 2rem;
    border-bottom: 1px solid var(--border-color);
    max-width: 1200px;
    margin: 0 auto;
    font-size: 0.9rem;
}

.breadcrumbs a {
    color: var(--link-color);
    text-decoration: none;
}

.breadcrumbs a:hover {
    text-decoration: underline;
}

/* Container Layout */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
    display: grid;
    grid-template-columns: 1fr 300px;
    gap: 2rem;
}

/* Main Content */
.content {
    background-color: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.content h1 {
    color: var(--primary-color);
    font-size: 2.5rem;
    margin-bottom: 1rem;
    border-bottom: 3px solid var(--secondary-color);
    padding-bottom: 1rem;
}

.content h2 {
    color: var(--secondary-color);
    font-size: 1.8rem;
    margin-top: 1.5rem;
    margin-bottom: 0.5rem;
}

.content h3 {
    color: var(--accent-color);
    font-size: 1.3rem;
    margin-top: 1rem;
    margin-bottom: 0.5rem;
}

.content p {
    margin-bottom: 1rem;
    text-align: justify;
}

.content blockquote {
    border-left: 4px solid var(--secondary-color);
    padding-left: 1rem;
    margin: 1rem 0;
    color: #555;
    font-style: italic;
}

/* Tables */
.anatomy-table {
    width: 100%;
    margin: 1rem 0;
    border-collapse: collapse;
    background-color: white;
}

.anatomy-table th,
.anatomy-table td {
    border: 1px solid var(--border-color);
    padding: 0.75rem;
    text-align: left;
}

.anatomy-table th {
    background-color: var(--light-bg);
    font-weight: bold;
    color: var(--primary-color);
}

.anatomy-table tr:nth-child(even) {
    background-color: #f9f9f9;
}

.anatomy-table tr:hover {
    background-color: #f0f0f0;
}

/* Links */
.wiki-link {
    color: var(--secondary-color);
    text-decoration: none;
    font-weight: 500;
    transition: all 0.3s;
    border-bottom: 2px solid transparent;
}

.wiki-link:hover {
    border-bottom-color: var(--secondary-color);
    background-color: rgba(231, 76, 60, 0.1);
    padding: 0.1rem 0.2rem;
    border-radius: 2px;
}

.dead-link {
    color: #999;
    text-decoration: line-through;
    cursor: not-allowed;
}

code {
    background-color: #f4f4f4;
    padding: 0.2rem 0.4rem;
    border-radius: 3px;
    font-family: 'Courier New', monospace;
}

/* Sidebar */
.sidebar {
    display: flex;
    flex-direction: column;
    gap: 2rem;
}

.sidebar-section {
    background-color: white;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.sidebar-section h3 {
    color: var(--secondary-color);
    margin-bottom: 1rem;
    font-size: 1.1rem;
}

.sidebar-section ul {
    list-style: none;
}

.sidebar-section li {
    margin-bottom: 0.5rem;
}

.sidebar-section a {
    color: var(--link-color);
    text-decoration: none;
    transition: all 0.3s;
}

.sidebar-section a:hover {
    color: var(--primary-color);
    margin-left: 0.3rem;
}

.sidebar-section p {
    font-size: 0.9rem;
    line-height: 1.5;
}

/* Index Page */
.index-page {
    text-align: center;
}

.index-page h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.index-page blockquote {
    font-size: 1.2rem;
    color: #666;
    margin: 2rem 0;
}

/* Footer */
footer {
    background-color: var(--primary-color);
    color: white;
    text-align: center;
    padding: 2rem;
    margin-top: 3rem;
}

/* Responsive Design */
@media (max-width: 768px) {
    .container {
        grid-template-columns: 1fr;
    }

    .nav-container {
        flex-direction: column;
        gap: 1rem;
    }

    .nav-search input {
        min-width: 100%;
    }

    .content {
        padding: 1rem;
    }

    .content h1 {
        font-size: 1.8rem;
    }

    .content h2 {
        font-size: 1.4rem;
    }

    .anatomy-table {
        font-size: 0.9rem;
    }

    .anatomy-table th,
    .anatomy-table td {
        padding: 0.5rem;
    }
}
"""

        css_file = self.output_path / 'styles.css'
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(css_content)

        # Create JavaScript file
        js_content = """// AnatomyLink Interactive Features

document.addEventListener('DOMContentLoaded', function() {
    // Search functionality
    const searchBox = document.getElementById('search-box');
    if (searchBox) {
        searchBox.addEventListener('input', debounce(handleSearch, 300));
    }

    // Smooth scroll for internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // Highlight current page in navigation
    highlightCurrentPage();
});

function handleSearch(e) {
    const query = e.target.value.toLowerCase();
    if (query.length < 2) return;

    // This could be extended to search the content
    console.log('Search:', query);
}

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function highlightCurrentPage() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('a[href]').forEach(link => {
        if (link.getAttribute('href').endsWith(currentPage)) {
            link.classList.add('active');
        }
    });
}
"""

        js_file = self.output_path / 'script.js'
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(js_content)

        print("  ✓ styles.css created")
        print("  ✓ script.js created")

def main():
    builder = AnatomyLinkBuilder(VAULT_PATH, OUTPUT_PATH)
    builder.scan_vault()
    builder.build_site()

    print("\n✨ Done! Open this file in a browser:")
    print(f"   {OUTPUT_PATH / 'index.html'}")

if __name__ == '__main__':
    main()
