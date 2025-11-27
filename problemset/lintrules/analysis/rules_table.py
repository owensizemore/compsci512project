#!/usr/bin/env python3
"""
Create a table of the top 20 lint rules with explanations and best practices.
Data source: flake8 lint output
Reference: https://www.flake8rules.com/
"""

import glob
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Comprehensive lint rule descriptions from flake8rules.com
LINT_RULES = {
    'E111': {
        'name': 'indentation is not a multiple of four',
        'explanation': 'Indentation should use multiples of 4 spaces (PEP 8 standard)',
        'example': 'def foo():\n  return 1  # Wrong: 2 spaces',
        'fix': 'Use 4 spaces per indentation level consistently'
    },
    'E112': {
        'name': 'expected an indented block',
        'explanation': 'Missing indentation after a colon statement',
        'example': 'if True:\nprint("bad")  # Missing indent',
        'fix': 'Add proper indentation after colon (:)'
    },
    'E117': {
        'name': 'over-indented',
        'explanation': 'Line has too much indentation',
        'example': 'def foo():\n        return 1  # 8 spaces instead of 4',
        'fix': 'Reduce indentation to appropriate level'
    },
    'E201': {
        'name': 'whitespace after "("',
        'explanation': 'Unnecessary space after opening bracket/parenthesis',
        'example': 'func( arg)  # Extra space after (',
        'fix': 'Remove space: func(arg)'
    },
    'E202': {
        'name': 'whitespace before ")"',
        'explanation': 'Unnecessary space before closing bracket/parenthesis',
        'example': 'func(arg )  # Extra space before )',
        'fix': 'Remove space: func(arg)'
    },
    'E203': {
        'name': 'whitespace before ":"',
        'explanation': 'Unnecessary space before colon',
        'example': 'x[1 :]  # Space before colon',
        'fix': 'Remove space: x[1:]'
    },
    'E211': {
        'name': 'whitespace before "("',
        'explanation': 'Unnecessary space before opening parenthesis',
        'example': 'func (arg)  # Space before (',
        'fix': 'Remove space: func(arg)'
    },
    'E225': {
        'name': 'missing whitespace around operator',
        'explanation': 'Binary operators should have spaces on both sides',
        'example': 'x=1+2  # Missing spaces around = and +',
        'fix': 'Add spaces: x = 1 + 2'
    },
    'E228': {
        'name': 'missing whitespace around modulo operator',
        'explanation': 'Modulo operator should have spaces on both sides',
        'example': 'x = 10%3  # Missing spaces around %',
        'fix': 'Add spaces: x = 10 % 3'
    },
    'E231': {
        'name': 'missing whitespace after ","',
        'explanation': 'Comma should be followed by a space',
        'example': 'func(a,b,c)  # Missing spaces after commas',
        'fix': 'Add spaces: func(a, b, c)'
    },
    'E265': {
        'name': 'block comment should start with "# "',
        'explanation': 'Comments should have a space after the hash',
        'example': '#comment  # Missing space after #',
        'fix': 'Add space: # comment'
    },
    'E275': {
        'name': 'missing whitespace after keyword',
        'explanation': 'Keywords like assert, raise should have space after them',
        'example': 'assert(x > 0)  # Missing space after assert',
        'fix': 'Add space: assert (x > 0)'
    },
    'E302': {
        'name': 'expected 2 blank lines, found N',
        'explanation': 'Top-level functions/classes need 2 blank lines before them',
        'example': 'def foo():\n    pass\ndef bar():  # Only 0 lines',
        'fix': 'Add 2 blank lines before function/class definitions'
    },
    'E303': {
        'name': 'too many blank lines (N)',
        'explanation': 'Too many consecutive blank lines',
        'example': 'x = 1\n\n\n\ny = 2  # 4 blank lines',
        'fix': 'Remove extra blank lines (max 2)'
    },
    'E305': {
        'name': 'expected 2 blank lines after class or function definition',
        'explanation': 'Need 2 blank lines after top-level definitions',
        'example': 'def foo():\n    pass\ncode()  # Missing blank lines',
        'fix': 'Add 2 blank lines after top-level definitions'
    },
    'E401': {
        'name': 'multiple imports on one line',
        'explanation': 'Each import should be on its own line',
        'example': 'import os, sys  # Multiple imports',
        'fix': 'Split: import os\\nimport sys'
    },
    'E501': {
        'name': 'line too long (N > 79 characters)',
        'explanation': 'Lines should not exceed 79 characters (PEP 8)',
        'example': 'x = very_long_function_name(arg1, arg2, arg3, arg4, arg5, arg6)',
        'fix': 'Break long lines with parentheses or backslashes'
    },
    'E701': {
        'name': 'multiple statements on one line (colon)',
        'explanation': 'Compound statements should not be on one line',
        'example': 'if x: print(x)  # Statement on same line',
        'fix': 'Split: if x:\\n    print(x)'
    },
    'E703': {
        'name': 'statement ends with a semicolon',
        'explanation': 'Python does not require semicolons at end of lines',
        'example': 'x = 1;  # Unnecessary semicolon',
        'fix': 'Remove semicolon: x = 1'
    },
    'E712': {
        'name': 'comparison to True should be "if cond is True:" or "if cond:"',
        'explanation': 'Do not use == or != with True/False/None',
        'example': 'if x == True:  # Wrong comparison',
        'fix': 'Use: if x: or if x is True:'
    },
    'E741': {
        'name': 'ambiguous variable name',
        'explanation': 'Avoid single-letter names like l, O, I that look like numbers',
        'example': 'l = [1, 2, 3]  # l looks like 1',
        'fix': 'Use descriptive names: list_items = [1, 2, 3]'
    },
    'E743': {
        'name': 'ambiguous function name',
        'explanation': 'Avoid function names like l, O, I',
        'example': 'def l():  # l looks like 1',
        'fix': 'Use descriptive names: def load():'
    },
    'E999': {
        'name': 'SyntaxError or IndentationError',
        'explanation': 'Code has a syntax error that prevents parsing',
        'example': 'def foo(  # Unclosed parenthesis',
        'fix': 'Fix the syntax error in the code'
    },
    'F401': {
        'name': 'module imported but unused',
        'explanation': 'Imported module is never used in the code',
        'example': 'import os  # os is never used',
        'fix': 'Remove unused imports or use the module'
    },
    'F821': {
        'name': 'undefined name',
        'explanation': 'Variable or function used before being defined',
        'example': 'print(x)  # x is not defined',
        'fix': 'Define variable before use: x = 1'
    },
    'W191': {
        'name': 'indentation contains tabs',
        'explanation': 'Use spaces instead of tabs for indentation',
        'example': 'def foo():\n\treturn 1  # Tab used',
        'fix': 'Replace tabs with 4 spaces'
    },
    'W291': {
        'name': 'trailing whitespace',
        'explanation': 'Unnecessary whitespace at end of line',
        'example': 'x = 1   # Spaces after 1',
        'fix': 'Remove trailing spaces at end of line'
    },
    'W293': {
        'name': 'blank line contains whitespace',
        'explanation': 'Empty lines should not contain spaces or tabs',
        'example': 'x = 1\n    \ny = 2  # Spaces on blank line',
        'fix': 'Remove all whitespace from blank lines'
    },
    'W391': {
        'name': 'blank line at end of file',
        'explanation': 'File should not end with blank lines',
        'example': 'x = 1\n\n\n# Extra blank lines at EOF',
        'fix': 'Remove trailing blank lines at end of file'
    },
}


def load_lint_data(file_pattern):
    """Load lint rule data and count occurrences."""
    rule_counts = defaultdict(int)

    for filepath in glob.glob(file_pattern):
        with open(filepath, 'r') as f:
            for line in f:
                parts = line.strip().split('\t')
                if len(parts) >= 3:
                    construct = parts[1].strip()
                    count = int(parts[2].strip())

                    # Extract rule code (remove LINT_ prefix)
                    if construct.startswith('LINT_'):
                        rule_code = construct.replace('LINT_', '')
                        rule_counts[rule_code] += count

    return rule_counts


def create_rules_table(rule_counts, top_n=20):
    """Create a formatted table of top lint rules."""
    # Sort by count and take top N
    sorted_rules = sorted(rule_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]

    if not sorted_rules:
        print("No lint data to display")
        return

    # Print text table
    print("\n" + "=" * 120)
    print(f"{'Rank':<6}{'Rule':<8}{'Count':<8}{'Description':<40}{'Best Practice':<60}")
    print("=" * 120)

    for rank, (rule_code, count) in enumerate(sorted_rules, 1):
        rule_info = LINT_RULES.get(rule_code, {
            'name': 'Unknown rule',
            'explanation': 'No description available',
            'fix': 'Refer to flake8 documentation'
        })

        # Truncate long descriptions for table display
        name = rule_info['name'][:38]
        fix = rule_info['fix'][:58]

        print(f"{rank:<6}{rule_code:<8}{count:<8}{name:<40}{fix:<60}")

    print("=" * 120 + "\n")

    return sorted_rules


def create_visual_table(sorted_rules):
    """Create a visual matplotlib table."""
    fig, ax = plt.subplots(figsize=(18, 12))
    ax.axis('tight')
    ax.axis('off')

    # Prepare table data
    table_data = []
    headers = ['Rank', 'Rule', 'Count', 'Description', 'Best Practice']

    for rank, (rule_code, count) in enumerate(sorted_rules, 1):
        rule_info = LINT_RULES.get(rule_code, {
            'name': 'Unknown rule',
            'fix': 'Refer to flake8 documentation'
        })

        # Wrap text for better display
        name = rule_info['name']
        fix = rule_info['fix']

        # Limit length for visual clarity
        if len(name) > 50:
            name = name[:47] + '...'
        if len(fix) > 60:
            fix = fix[:57] + '...'

        table_data.append([
            str(rank),
            rule_code,
            str(count),
            name,
            fix
        ])

    # Create table
    table = ax.table(cellText=table_data, colLabels=headers,
                     cellLoc='left', loc='center',
                     colWidths=[0.06, 0.08, 0.08, 0.35, 0.43])

    # Style the table
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 2.5)

    # Style header
    for i in range(len(headers)):
        cell = table[(0, i)]
        cell.set_facecolor('#4472C4')
        cell.set_text_props(weight='bold', color='white', fontsize=10)

    # Alternate row colors
    for i in range(1, len(table_data) + 1):
        for j in range(len(headers)):
            cell = table[(i, j)]
            if i % 2 == 0:
                cell.set_facecolor('#E7E6E6')
            else:
                cell.set_facecolor('#FFFFFF')

            # Highlight count column
            if j == 2:
                cell.set_text_props(weight='bold')

    # Title
    plt.title('Top 20 Most Common Flake8 Lint Rules\n(with descriptions and best practices)',
              fontsize=16, fontweight='bold', pad=20)

    plt.tight_layout()
    return fig


def create_detailed_report(sorted_rules, output_file='lint_rules_detailed.txt'):
    """Create a detailed text report with full descriptions."""
    with open(output_file, 'w') as f:
        f.write("=" * 100 + "\n")
        f.write("DETAILED LINT RULES REPORT\n")
        f.write("Top 20 Most Common Flake8 Lint Rules\n")
        f.write("=" * 100 + "\n\n")

        for rank, (rule_code, count) in enumerate(sorted_rules, 1):
            rule_info = LINT_RULES.get(rule_code, {
                'name': 'Unknown rule',
                'explanation': 'No description available',
                'example': 'N/A',
                'fix': 'Refer to flake8 documentation'
            })

            f.write(f"{'=' * 100}\n")
            f.write(f"#{rank} - {rule_code}: {rule_info['name']}\n")
            f.write(f"{'=' * 100}\n")
            f.write(f"Occurrences: {count:,}\n\n")
            f.write(f"EXPLANATION:\n{rule_info['explanation']}\n\n")
            f.write(f"EXAMPLE:\n{rule_info['example']}\n\n")
            f.write(f"BEST PRACTICE:\n{rule_info['fix']}\n\n")

    return output_file


def main():
    # Load data from output files
    print("Loading lint rule data from output files...")
    file_pattern = 'problemset/lintrules/output/output-run3_part-*'
    rule_counts = load_lint_data(file_pattern)

    print(f"Found {len(rule_counts)} unique lint rules")
    print(f"Total violations: {sum(rule_counts.values()):,}")

    # Create and display text table
    sorted_rules = create_rules_table(rule_counts, top_n=20)

    if sorted_rules:
        # Create visual table
        print("Creating visual table...")
        fig = create_visual_table(sorted_rules)

        output_path = 'problemset/lintrules/analysis/rules_table.png'
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"Visual table saved to: {output_path}")

        # Create detailed report
        print("\nCreating detailed report...")
        report_path = 'problemset/lintrules/analysis/lint_rules_detailed.txt'
        create_detailed_report(sorted_rules, report_path)
        print(f"Detailed report saved to: {report_path}")

        plt.show()


if __name__ == '__main__':
    main()
