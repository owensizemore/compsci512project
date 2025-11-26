#!/usr/bin/env python3
"""
Analyze import popularity by calculating the percentage of files that use each import.
"""

import matplotlib.pyplot as plt
from collections import defaultdict
import glob


def load_import_data(file_pattern):
    """Load import data and track which files use which imports."""
    import_files = defaultdict(set)  # import_name -> set of files
    all_files = set()

    for filepath in glob.glob(file_pattern):
        with open(filepath, 'r') as f:
            for line in f:
                parts = line.strip().split('\t')
                if len(parts) >= 3:
                    filename = parts[0].strip()
                    construct = parts[1].strip()

                    # Track all unique files
                    all_files.add(filename)

                    # Only process import constructs
                    if construct.startswith('IMPORT_') or construct.startswith('IMPORT_FROM_'):
                        # Store which file uses this import
                        import_files[construct].add(filename)

    return import_files, all_files


def calculate_import_percentages(import_files, all_files):
    """Calculate the percentage of files that use each import."""
    total_files = len(all_files)

    if total_files == 0:
        return {}

    import_percentages = {}
    for import_name, files in import_files.items():
        percentage = (len(files) / total_files) * 100
        import_percentages[import_name] = {
            'percentage': percentage,
            'file_count': len(files),
            'total_files': total_files
        }

    return import_percentages


def format_import_label(import_name):
    """Format import names for display."""
    # Remove IMPORT_ or IMPORT_FROM_ prefix
    if import_name.startswith('IMPORT_FROM_'):
        label = import_name.replace('IMPORT_FROM_', '')
        # Format as "from module import name"
        if '.' in label:
            module, name = label.rsplit('.', 1)
            return f"from {module.lower()}\nimport {name.lower()}"
        return label.lower()
    elif import_name.startswith('IMPORT_'):
        label = import_name.replace('IMPORT_', '')
        return f"import {label.lower()}"
    return import_name.lower()


def create_import_popularity_chart(import_percentages, top_n=20):
    """Create a bar chart showing the most popular imports."""
    # Sort by percentage and take top N
    sorted_imports = sorted(import_percentages.items(),
                            key=lambda x: x[1]['percentage'],
                            reverse=True)[:top_n]

    if not sorted_imports:
        print("No import data to visualize")
        return

    # Prepare data
    labels = [format_import_label(imp) for imp, _ in sorted_imports]
    percentages = [data['percentage'] for _, data in sorted_imports]
    file_counts = [data['file_count'] for _, data in sorted_imports]

    # Create color gradient from dark to light
    colors = plt.cm.viridis([i / len(labels) for i in range(len(labels))])

    # Create figure
    fig, ax = plt.subplots(figsize=(14, 10))

    # Create horizontal bar chart
    bars = ax.barh(range(len(labels)), percentages, color=colors,
                   alpha=0.8, edgecolor='white', linewidth=2)

    # Set labels
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xlabel('Percentage of Files (%)', fontsize=12, fontweight='bold')
    ax.set_title(f'Top {top_n} Most Popular Python Imports\n(By percentage of files using the import)',
                 fontsize=14, fontweight='bold', pad=20)

    # Add percentage labels on bars
    for i, (bar, pct, count) in enumerate(zip(bars, percentages, file_counts)):
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height() / 2,
                f' {pct:.1f}% ({count} files)',
                ha='left', va='center', fontsize=9, fontweight='bold')

    # Add grid for readability
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)

    # Invert y-axis so highest is at top
    ax.invert_yaxis()

    # Set x-axis limit to give space for labels
    ax.set_xlim(0, max(percentages) * 1.3)

    plt.tight_layout()
    return fig


def main():
    # Load data from output files
    print("Loading import data from output files...")
    file_pattern = 'problemset/languagestructures/output/output-run1_part-*'
    import_files, all_files = load_import_data(file_pattern)

    print(f"Found {len(all_files)} unique files")
    print(f"Found {len(import_files)} unique imports")

    # Calculate percentages
    import_percentages = calculate_import_percentages(import_files, all_files)

    # Print top 10 imports
    print("\nTop 10 most popular imports:")
    sorted_imports = sorted(import_percentages.items(),
                            key=lambda x: x[1]['percentage'],
                            reverse=True)[:10]
    for import_name, data in sorted_imports:
        print(f"  {import_name}: {data['percentage']:.2f}% ({data['file_count']} files)")

    # Create chart
    print("\nCreating import popularity chart...")
    fig = create_import_popularity_chart(import_percentages, top_n=20)

    if fig:
        # Save the figure
        output_path = 'problemset/languagestructures/analysis/import_popularity.png'
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"Chart saved to: {output_path}")

        # Show the plot
        plt.show()


if __name__ == '__main__':
    main()
