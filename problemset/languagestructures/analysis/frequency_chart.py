#!/usr/bin/env python3
import matplotlib.pyplot as plt
from collections import defaultdict
import glob

CATEGORY_LABELS = {
    'SYNTAX_ERROR': 'Syntax Error',
    'IMPORT': 'Imports',
    'IMPORT_FROM': 'Imports',
    'BOOLEAN_OP': 'Boolean',
    'OPERATOR': 'Binary Operation',
    'UNARY_OP': 'Unary Operation',
    'COMPARE_OP': 'Comparison',
    'CONTROL_IF': 'If Statement',
    'CONTROL_ELSE': 'Else Statement',
    'CONTROL_WHILE': 'While Loop',
    'CONTROL_FOR': 'For Loop',
    'FUNCTION_DEF': 'Create Function',
    'DATA_LIST': 'List',
    'DATA_DICT': 'Dict',
    'DATA_SET': 'Set'
}

CATEGORY_COLORS = {
    'Syntax Error': '#e74c3c',
    'Imports': '#3498db',
    'Boolean': '#9b59b6',
    'Binary Operation': '#e67e22',
    'Unary Operation': '#f39c12',
    'Comparison': '#1abc9c',
    'If Statement': '#2ecc71',
    'Else Statement': '#27ae60',
    'While Loop': '#16a085',
    'For Loop': '#2980b9',
    'Create Function': '#8e44ad',
    'List': '#c0392b',
    'Dict': '#d35400',
    'Set': '#f39c12'
}


def categorize_construct(construct):
    """Categorize a construct based on its prefix."""
    for prefix, label in CATEGORY_LABELS.items():
        if construct.startswith(prefix):
            return label
    return 'Other'


def load_data(file_pattern):
    """Load and aggregate data from output files."""
    counts = defaultdict(int)

    for filepath in glob.glob(file_pattern):
        with open(filepath, 'r') as f:
            for line in f:
                parts = line.strip().split('\t')
                if len(parts) >= 3:
                    construct = parts[1].strip()
                    count = int(parts[2].strip())
                    counts[construct] += count

    return counts


def aggregate_by_category(counts):
    """Aggregate construct counts by category."""
    category_counts = defaultdict(int)

    for construct, count in counts.items():
        category = categorize_construct(construct)
        category_counts[category] += count

    return category_counts


def create_bar_chart(category_counts):
    """Create a bar chart visualization sorted by frequency."""
    # Filter out 'Other' category and sort by count (highest to lowest)
    categories = [(cat, count) for cat, count in category_counts.items() if cat != 'Other']
    categories.sort(key=lambda x: x[1], reverse=True)

    if not categories:
        print("No data to visualize")
        return

    # Prepare data
    labels = [cat for cat, _ in categories]
    counts = [count for _, count in categories]
    colors = [CATEGORY_COLORS.get(cat, '#95a5a6') for cat in labels]

    # Create figure
    fig, ax = plt.subplots(figsize=(12, 8))

    # Create bar chart
    bars = ax.barh(range(len(labels)), counts, color=colors, alpha=0.8, edgecolor='white', linewidth=2)

    # Set labels
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=12)
    ax.set_xlabel('Frequency', fontsize=14, fontweight='bold')
    ax.set_title('Python Language Construct Usage Analysis\n(Sorted by Frequency)',
                 fontsize=16, fontweight='bold', pad=20)

    # Add value labels on bars
    for i, (bar, count) in enumerate(zip(bars, counts)):
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height() / 2,
                f' {count:,}',
                ha='left', va='center', fontsize=10, fontweight='bold')

    # Add grid for readability
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)

    # Invert y-axis so highest is at top
    ax.invert_yaxis()

    plt.tight_layout()
    return fig


def main():
    # Load data from output files
    print("Loading data from output files...")
    file_pattern = 'problemset/languagestructures/output/output-run1_part-*'
    counts = load_data(file_pattern)

    print(f"Loaded {len(counts)} unique constructs")

    # Aggregate by category
    category_counts = aggregate_by_category(counts)

    print("\nCategory counts:")
    for cat, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat}: {count:,}")

    # Create bar chart
    print("\nCreating bar chart...")
    fig = create_bar_chart(category_counts)

    if fig:
        # Save the figure
        output_path = 'problemset/languagestructures/analysis/frequency_chart.png'
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"Bar chart saved to: {output_path}")

        # Show the plot
        plt.show()


# cd /Users/owensizemore/code/duke/compsci512project && python3 problemset/languagestructures/analysis/frequency_chart.py
if __name__ == '__main__':
    main()
