#!/usr/bin/env python3
"""
Analyze correlations between different programming errors.
Shows which errors tend to occur together in the same files.
"""

import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import glob


def load_error_data(file_pattern):
    """Load error data and track which files have which errors."""
    file_errors = defaultdict(set)  # filename -> set of error types
    all_errors = set()

    for filepath in glob.glob(file_pattern):
        with open(filepath, 'r') as f:
            for line in f:
                parts = line.strip().split('\t')
                if len(parts) >= 3:
                    filename = parts[0].strip()
                    construct = parts[1].strip()

                    # Only process error and warning constructs
                    if construct.startswith('ERROR_') or construct.startswith('WARNING_'):
                        # Normalize undefined variable errors to a single category
                        if construct.startswith('ERROR_NAME_UNDEFINED_'):
                            construct = 'ERROR_NAME_UNDEFINED'

                        file_errors[filename].add(construct)
                        all_errors.add(construct)

    return file_errors, all_errors


def calculate_correlation_matrix(file_errors, all_errors):
    """Calculate correlation matrix between different error types."""
    error_list = sorted(list(all_errors))
    n = len(error_list)

    # Create a matrix to count co-occurrences
    co_occurrence = np.zeros((n, n), dtype=int)
    error_counts = defaultdict(int)

    # Count occurrences and co-occurrences
    for filename, errors in file_errors.items():
        for error in errors:
            error_counts[error] += 1

        # Count co-occurrences
        for i, error1 in enumerate(error_list):
            for j, error2 in enumerate(error_list):
                if error1 in errors and error2 in errors:
                    co_occurrence[i, j] += 1

    # Calculate correlation coefficients (Jaccard similarity)
    correlation = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                correlation[i, j] = 1.0
            else:
                # Jaccard similarity: intersection / union
                intersection = co_occurrence[i, j]
                union = error_counts[error_list[i]] + error_counts[error_list[j]] - intersection
                if union > 0:
                    correlation[i, j] = intersection / union
                else:
                    correlation[i, j] = 0

    return correlation, error_list, error_counts


def format_error_label(error_name):
    """Format error names for display."""
    # Remove ERROR_ or WARNING_ prefix
    label = error_name.replace('ERROR_', '').replace('WARNING_', '')

    # Convert to title case and replace underscores
    label = label.replace('_', ' ').title()

    return label


def create_correlation_heatmap(correlation, error_list, error_counts):
    """Create a heatmap showing correlations between errors."""
    if len(error_list) == 0:
        print("No error data to visualize")
        return

    # Format labels with counts
    labels = [f"{format_error_label(err)}\n(n={error_counts[err]})" for err in error_list]

    # Create figure with appropriate size
    fig_size = max(10, len(error_list) * 0.8)
    fig, ax = plt.subplots(figsize=(fig_size, fig_size))

    # Create heatmap
    im = ax.imshow(correlation, cmap='YlOrRd', aspect='auto', vmin=0, vmax=1)

    # Set ticks and labels
    ax.set_xticks(range(len(error_list)))
    ax.set_yticks(range(len(error_list)))
    ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=9)
    ax.set_yticklabels(labels, fontsize=9)

    # Add colorbar
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Correlation Coefficient\n(Jaccard Similarity)', rotation=270, labelpad=20, fontsize=11)

    # Add correlation values in cells
    for i in range(len(error_list)):
        for j in range(len(error_list)):
            if i != j and correlation[i, j] > 0.05:  # Only show significant correlations
                text = ax.text(j, i, f'{correlation[i, j]:.2f}',
                               ha='center', va='center', color='black' if correlation[i, j] < 0.5 else 'white',
                               fontsize=8, fontweight='bold')

    # Title
    ax.set_title('Programming Error Correlations\n(Shows which errors tend to occur together)',
                 fontsize=14, fontweight='bold', pad=20)

    # Grid
    ax.set_xticks(np.arange(len(error_list)) - 0.5, minor=True)
    ax.set_yticks(np.arange(len(error_list)) - 0.5, minor=True)
    ax.grid(which='minor', color='white', linestyle='-', linewidth=2)

    plt.tight_layout()
    return fig


def print_top_correlations(correlation, error_list, top_n=10):
    """Print the top correlated error pairs."""
    correlations_list = []

    for i in range(len(error_list)):
        for j in range(i + 1, len(error_list)):  # Only upper triangle to avoid duplicates
            if correlation[i, j] > 0:
                correlations_list.append((error_list[i], error_list[j], correlation[i, j]))

    # Sort by correlation coefficient
    correlations_list.sort(key=lambda x: x[2], reverse=True)

    print(f"\nTop {top_n} correlated error pairs:")
    for i, (err1, err2, corr) in enumerate(correlations_list[:top_n], 1):
        print(f"  {i}. {format_error_label(err1)} <-> {format_error_label(err2)}: {corr:.3f}")


def create_network_graph(correlation, error_list, error_counts, threshold=0.2):
    """Create a network graph showing strong correlations."""
    import matplotlib.patches as mpatches

    fig, ax = plt.subplots(figsize=(14, 10))

    # Filter errors with significant correlations
    n = len(error_list)
    positions = {}

    # Arrange nodes in a circle
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    radius = 3
    for i, error in enumerate(error_list):
        positions[error] = (radius * np.cos(angles[i]), radius * np.sin(angles[i]))

    # Draw edges for correlations above threshold
    for i in range(n):
        for j in range(i + 1, n):
            if correlation[i, j] > threshold:
                x1, y1 = positions[error_list[i]]
                x2, y2 = positions[error_list[j]]

                # Line thickness based on correlation strength
                linewidth = correlation[i, j] * 5
                alpha = min(correlation[i, j] + 0.3, 0.9)

                ax.plot([x1, x2], [y1, y2], 'b-', linewidth=linewidth, alpha=alpha, zorder=1)

    # Draw nodes
    for error in error_list:
        x, y = positions[error]
        # Node size based on error frequency
        size = np.sqrt(error_counts[error]) * 50
        ax.scatter(x, y, s=size, c='red', alpha=0.7, edgecolors='darkred', linewidth=2, zorder=2)

        # Add label
        label = format_error_label(error)
        ax.text(x * 1.15, y * 1.15, label, ha='center', va='center', fontsize=9,
                fontweight='bold', bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

    # Set axis properties
    ax.set_xlim(-radius * 1.5, radius * 1.5)
    ax.set_ylim(-radius * 1.5, radius * 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Title
    plt.title(f'Programming Error Network\n(Edges show correlations > {threshold:.1%})',
              fontsize=14, fontweight='bold', pad=20)

    # Legend
    legend_elements = [
        mpatches.Patch(color='red', alpha=0.7, label='Error Type (size = frequency)'),
        mpatches.Patch(color='blue', alpha=0.5, label=f'Correlation > {threshold:.1%}')
    ]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=10)

    plt.tight_layout()
    return fig


def main():
    # Load data from output files
    print("Loading error data from output files...")
    file_pattern = 'problemset/programmingerrors/output/output-run2_part-*'
    file_errors, all_errors = load_error_data(file_pattern)

    print(f"Found {len(file_errors)} files with errors")
    print(f"Found {len(all_errors)} unique error types")

    # Calculate correlation matrix
    print("\nCalculating error correlations...")
    correlation, error_list, error_counts = calculate_correlation_matrix(file_errors, all_errors)

    # Print error frequencies
    print("\nError frequencies:")
    for error in sorted(error_counts.keys(), key=lambda x: error_counts[x], reverse=True):
        print(f"  {format_error_label(error)}: {error_counts[error]} files")

    # Print top correlations
    print_top_correlations(correlation, error_list, top_n=15)

    # Create correlation heatmap
    print("\nCreating correlation heatmap...")
    fig1 = create_correlation_heatmap(correlation, error_list, error_counts)

    if fig1:
        output_path1 = 'problemset/programmingerrors/analysis/correlation_heatmap.png'
        plt.savefig(output_path1, dpi=300, bbox_inches='tight')
        print(f"Heatmap saved to: {output_path1}")

    # Create network graph
    print("\nCreating correlation network graph...")
    fig2 = create_network_graph(correlation, error_list, error_counts, threshold=0.15)

    if fig2:
        output_path2 = 'problemset/programmingerrors/analysis/correlation_network.png'
        plt.savefig(output_path2, dpi=300, bbox_inches='tight')
        print(f"Network graph saved to: {output_path2}")

    plt.show()


if __name__ == '__main__':
    main()
