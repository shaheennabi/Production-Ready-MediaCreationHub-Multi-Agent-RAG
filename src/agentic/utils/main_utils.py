import re



# Then, simplify the image formatting function to preserve markdown
def format_markdown_images(markdown_text):
    """
    Keep markdown image syntax intact and just ensure URLs are properly formatted
    """
    import re
    
    # Only process markdown images without converting to HTML
    img_pattern = r'!\[(.*?)\]\((.*?)\)'
    
    def fix_url(match):
        alt_text, url = match.groups()
        url = url.strip()
        if not url.startswith(('http://', 'https://')):
            url = f"https:{url}" if url.startswith('//') else f"https://{url}"
        return f'![{alt_text}]({url})'
    
    return re.sub(img_pattern, fix_url, markdown_text)



@classmethod
class LoadModel:
    pass