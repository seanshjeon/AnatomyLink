import re
import os
import json
from pathlib import Path
from urllib.parse import quote

class MarkdownToHTMLConverter:
    """Converts Obsidian-style markdown to HTML with wiki link support"""

    def __init__(self, file_index):
        """
        Initialize converter with file index
        file_index: dict mapping file titles to their paths
        """
        self.file_index = file_index

    def convert_wiki_links(self, text):
        """Convert [[link]] to HTML links"""
        # Pattern for [[page name]] or [[page name|display text]]
        pattern = r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]'

        def replace_link(match):
            page_name = match.group(1).strip()
            display_text = match.group(2).strip() if match.group(2) else page_name

            # Look up the file path for this page
            if page_name in self.file_index:
                file_path = self.file_index[page_name]
                # Convert file path to relative URL
                html_url = file_path.replace('.md', '.html').replace(' ', '%20')
                return f'<a href="{html_url}" class="wiki-link">{display_text}</a>'
            else:
                # If not found, create a dead link with special styling
                return f'<span class="dead-link" title="Not found: {page_name}">{display_text}</span>'

        return re.sub(pattern, replace_link, text)

    def convert_markdown_to_html(self, markdown_text):
        """Convert markdown text to HTML"""
        html = markdown_text

        # Remove YAML frontmatter
        html = re.sub(r'^---\n.*?\n---\n', '', html, flags=re.DOTALL)

        # Convert headings (# to ######)
        html = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
        html = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
        html = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)

        # Convert bold **text**
        html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)

        # Convert italic *text*
        html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)

        # Convert code `code`
        html = re.sub(r'`(.*?)`', r'<code>\1</code>', html)

        # Convert blockquotes > text
        html = re.sub(r'^> (.*?)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)

        # Convert tables
        html = self.convert_tables(html)

        # Convert wiki links
        html = self.convert_wiki_links(html)

        # Convert line breaks
        html = html.replace('\n\n', '</p><p>')
        html = '<p>' + html + '</p>'

        # Clean up multiple paragraph tags
        html = re.sub(r'</p>\s*<p>', '</p><p>', html)
        html = html.replace('<p></p>', '')

        return html

    def convert_tables(self, text):
        """Convert markdown tables to HTML"""
        lines = text.split('\n')
        result = []
        i = 0

        while i < len(lines):
            line = lines[i]

            # Check if this is a table header
            if '|' in line and i + 1 < len(lines) and '-' in lines[i + 1]:
                table_html = self.parse_table(lines, i)
                result.append(table_html['html'])
                i = table_html['end_index']
            else:
                result.append(line)
                i += 1

        return '\n'.join(result)

    def parse_table(self, lines, start_index):
        """Parse a markdown table and return HTML"""
        table_rows = []
        i = start_index

        # Parse header
        if '|' in lines[i]:
            headers = [h.strip() for h in lines[i].split('|')[1:-1]]
            table_rows.append(('header', headers))
            i += 1

        # Skip separator
        if i < len(lines) and '-' in lines[i]:
            i += 1

        # Parse body rows
        while i < len(lines) and '|' in lines[i]:
            cells = [c.strip() for c in lines[i].split('|')[1:-1]]
            if cells and any(cells):  # Only add non-empty rows
                table_rows.append(('body', cells))
            i += 1

        # Generate HTML
        html = '<table class="anatomy-table">\n'
        for row_type, cells in table_rows:
            tag = 'th' if row_type == 'header' else 'td'
            html += f'  <tr>\n'
            for cell in cells:
                html += f'    <{tag}>{cell}</{tag}>\n'
            html += f'  </tr>\n'
        html += '</table>\n'

        return {'html': html, 'end_index': i}
