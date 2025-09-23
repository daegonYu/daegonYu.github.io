#!/usr/bin/env python3
import re
import os
import glob
from datetime import datetime

def parse_filename(filename):
    """Parse the original blog filename to extract metadata."""
    # Parse pattern: [date]_[title]_[category]_[]_[description]_[].md
    pattern = r'\[(\d{8})\]_\[([^\]]+)\]_\[([^\]]*)\]_\[\]_\[([^\]]*)\]_\[\]\.md'
    match = re.match(pattern, os.path.basename(filename))

    if match:
        date_str, title, category, description = match.groups()
        # Convert date from YYYYMMDD to YYYY-MM-DD
        date_obj = datetime.strptime(date_str, '%Y%m%d')
        jekyll_date = date_obj.strftime('%Y-%m-%d')

        # Create safe filename for Jekyll
        safe_title = re.sub(r'[^a-zA-Z0-9\s-]', '', title).strip()
        safe_title = re.sub(r'\s+', '-', safe_title)
        jekyll_filename = f'{jekyll_date}-{safe_title.lower()}.md'
        jekyll_filename = re.sub(r'-+', '-', jekyll_filename)

        # Map categories to appropriate tags
        category_tags = {
            'LLM': ['llm', 'language-model', 'nlp'],
            'Embedding': ['embedding', 'retrieval', 'nlp'],
            'Encoder': ['encoder', 'bert', 'nlp'],
            'Synthetic': ['synthetic-data', 'data-generation', 'nlp'],
            '': ['research', 'nlp', 'machine-learning']
        }

        tags = category_tags.get(category, ['research', 'nlp', 'machine-learning'])

        return {
            'date': jekyll_date,
            'title': title,
            'category': category.lower() if category else 'blog',
            'description': description,
            'jekyll_filename': jekyll_filename,
            'original_filename': filename,
            'tags': tags
        }
    return None

def create_front_matter(metadata):
    """Create Jekyll front matter for the post."""
    tags_str = ', '.join(f'"{tag}"' for tag in metadata['tags'])

    front_matter = f"""---
layout: single
title: "{metadata['title']}"
date: {metadata['date']} 09:00:00 +0900
categories: ["{metadata['category']}"]
tags: [{tags_str}]
excerpt: "{metadata['description']}"
author_profile: true
read_time: true
comments: true
share: true
related: true
---

"""
    return front_matter

def convert_post(source_file, target_dir):
    """Convert a single blog post to Jekyll format."""
    metadata = parse_filename(source_file)
    if not metadata:
        print(f"Could not parse filename: {source_file}")
        return None

    # Read original content
    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {source_file}: {e}")
        return None

    # Create Jekyll post
    front_matter = create_front_matter(metadata)
    jekyll_content = front_matter + content

    # Write to target directory
    target_file = os.path.join(target_dir, metadata['jekyll_filename'])
    try:
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(jekyll_content)
        print(f"Converted: {os.path.basename(metadata['original_filename'])} -> {metadata['jekyll_filename']}")
        return target_file
    except Exception as e:
        print(f"Error writing {target_file}: {e}")
        return None

def convert_all_posts(source_dir, target_dir):
    """Convert all blog posts from source to target directory."""
    # Find all markdown files in source directory
    blog_files = glob.glob(os.path.join(source_dir, "*.md"))

    if not blog_files:
        print(f"No markdown files found in {source_dir}")
        return []

    # Ensure target directory exists
    os.makedirs(target_dir, exist_ok=True)

    converted_files = []
    failed_files = []

    for blog_file in blog_files:
        result = convert_post(blog_file, target_dir)
        if result:
            converted_files.append(result)
        else:
            failed_files.append(blog_file)

    print(f"\nConversion Summary:")
    print(f"Successfully converted: {len(converted_files)} posts")
    if failed_files:
        print(f"Failed to convert: {len(failed_files)} posts")
        for failed in failed_files:
            print(f"  - {os.path.basename(failed)}")

    return converted_files

# Test and main execution
if __name__ == "__main__":
    # Test with sample file
    test_file = '[20250316]_[Gemini Embedding Generalizable Embeddings from Gemini]_[Embedding]_[]_[현 최강 임베딩 모델 Gemini Embedding]_[].md'
    result = parse_filename(test_file)
    print("Testing filename parser:")
    print(f"Original: {test_file}")
    print(f"Parsed: {result}")

    if result:
        print(f"\nSample front matter:")
        print(create_front_matter(result))

    # Main conversion
    source_directory = "/tmp/study_blog/blog"
    target_directory = "C:/Users/유대곤/Desktop/vscode소스코드/dgyu.github.io/_posts"

    print(f"\nStarting conversion process...")
    print(f"Source: {source_directory}")
    print(f"Target: {target_directory}")

    converted = convert_all_posts(source_directory, target_directory)
    print(f"\nConversion complete! {len(converted)} posts converted.")