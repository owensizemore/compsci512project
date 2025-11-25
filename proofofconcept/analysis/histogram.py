#!/usr/bin/env python3
"""
Box-and-whisker plot of line counts from MapReduce output files.
"""

import matplotlib.pyplot as plt
import numpy as np
import os

# Read data from all three output files
output_files = [
    'output-run1_part-00000',
    'output-run1_part-00001',
    'output-run1_part-00002'
]

line_counts = []

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Read all line counts from the output files
for output_file in output_files:
    file_path = os.path.join(script_dir, output_file)
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                # Split by tab and get the second value (line count)
                parts = line.split('\t')
                if len(parts) == 2:
                    count = int(parts[1])
                    line_counts.append(count)

# Calculate statistics for outlier detection
q1 = np.percentile(line_counts, 25)
q3 = np.percentile(line_counts, 75)
iqr = q3 - q1

# Define outlier bounds using IQR method (1.5 * IQR)
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Identify outliers and non-outliers
outliers = [x for x in line_counts if x < lower_bound or x > upper_bound]
trimmed_counts = [x for x in line_counts if lower_bound <= x <= upper_bound]

# Calculate statistics on all data
mean_lines_all = np.mean(line_counts)
median_lines_all = np.median(line_counts)
max_lines = max(line_counts)
min_lines = min(line_counts)
total_files = len(line_counts)

# Calculate statistics on trimmed data
mean_lines_trimmed = np.mean(trimmed_counts)
median_lines_trimmed = np.median(trimmed_counts)

# Create the box-and-whisker plot with trimmed data (horizontal)
plt.figure(figsize=(12, 6))
bp = plt.boxplot(trimmed_counts, vert=False, patch_artist=True,
                 notch=True, showmeans=True,
                 boxprops=dict(facecolor='steelblue', alpha=0.7),
                 meanprops=dict(marker='D', markerfacecolor='red', markersize=8),
                 medianprops=dict(color='darkblue', linewidth=2),
                 whiskerprops=dict(linewidth=1.5),
                 capprops=dict(linewidth=1.5))

plt.xlabel('Line Count', fontsize=12)
plt.title('Distribution of Line Counts, P00018 (Outliers Trimmed)', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3, linestyle='--')

# Add statistics to the plot
num_outliers = len(outliers)
stats_text = f'Total Files: {total_files}\n'
stats_text += f'Files Shown: {len(trimmed_counts)}\n'
stats_text += f'Outliers Removed: {num_outliers}\n'
stats_text += f'Mean: {mean_lines_trimmed:.2f} lines (◆)\n'
stats_text += f'Median: {median_lines_trimmed:.2f} lines\n'
stats_text += f'Q1: {q1:.2f} lines\n'
stats_text += f'Q3: {q3:.2f} lines\n'
stats_text += f'IQR: {iqr:.2f} lines\n'
stats_text += f'Trimmed Range: {min(trimmed_counts)}-{max(trimmed_counts)} lines'

plt.text(0.98, 0.95, stats_text, transform=plt.gca().transAxes,
         fontsize=10, verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# Remove y-axis labels since there's only one box
plt.yticks([1], ['All Files'])

plt.tight_layout()

# Save the box plot
output_path = os.path.join(script_dir, 'line_count_boxplot.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Box-and-whisker plot saved to: {output_path}")

# Display the box plot
plt.show()

# Print summary statistics
print(f"\nSummary Statistics (All Data):")
print(f"Total files: {total_files}")
print(f"Mean line count: {mean_lines_all:.2f}")
print(f"Median line count: {median_lines_all:.2f}")
print(f"Min line count: {min_lines}")
print(f"Max line count: {max_lines}")

print(f"\nSummary Statistics (Trimmed Data):")
print(f"Files shown: {len(trimmed_counts)}")
print(f"Outliers removed: {len(outliers)}")
print(f"Mean line count: {mean_lines_trimmed:.2f}")
print(f"Median line count: {median_lines_trimmed:.2f}")
print(f"Q1 (25th percentile): {q1:.2f}")
print(f"Q3 (75th percentile): {q3:.2f}")
print(f"IQR (Interquartile Range): {iqr:.2f}")
print(f"Trimmed range: {min(trimmed_counts)}-{max(trimmed_counts)} lines")

if outliers:
    print(f"\nOutliers (removed from plot):")
    from collections import Counter

    outlier_freq = Counter(outliers)
    for count in sorted(outlier_freq.keys()):
        print(f"  {count} lines: {outlier_freq[count]} files")

print(f"\nLine count distribution (trimmed data):")
from collections import Counter

count_freq = Counter(trimmed_counts)
for count in sorted(count_freq.keys()):
    print(f"  {count} lines: {count_freq[count]} files")
