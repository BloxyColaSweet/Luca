"""Parse a file with a Lark grammar and write a visual HTML parse tree."""

import argparse
from dataclasses import dataclass, field
from html import escape
from pathlib import Path
import sys


from lark import Lark, Token, Tree
from lark.exceptions import LarkError

from lark.parsers.earley_forest import TreeForestTransformer
import re
import os


@dataclass
class _DiagramNode:
    label: str
    kind: str
    children: list["_DiagramNode"] = field(default_factory=list)
    width: float = 0
    x: float = 0
    depth: int = 0


def _build_diagram_node(node: Tree | Token, rule_priorities) -> _DiagramNode:
    if isinstance(node, Tree):
        
        try:
            return _DiagramNode(

                # NODE NAMING
                str(node.data + "." + str(0 if rule_priorities[node.data] is None else int(rule_priorities[node.data]))),
                "rule",
                [_build_diagram_node(child, rule_priorities) for child in node.children],
            )
        except:
            return _DiagramNode(

                # NODE NAMING
                str(node.data),
                "rule",
                [_build_diagram_node(child, rule_priorities) for child in node.children],
            )

    value = str(node)
    visible_value = value.strip()
    if not visible_value:
        visible_value = value.replace(" ", "␠").replace("\t", "⇥").replace("\n", "↵")
    return _DiagramNode(visible_value, "terminal")


def _measure_and_place(node: _DiagramNode, left: float = 0, depth: int = 0) -> float:
    label_width = max(24, len(node.label) * 10 + 12)
    node.depth = depth
    if not node.children:
        node.width = label_width
    else:
        child_widths = [_measure_and_place(child, 0, depth + 1) for child in node.children]
        children_width = sum(child_widths) + 24 * (len(child_widths) - 1)
        node.width = max(label_width, children_width)
        child_left = left + (node.width - children_width) / 2
        for child, child_width in zip(node.children, child_widths):
            _measure_and_place(child, child_left, depth + 1)
            child_left += child_width + 24

    node.x = left + node.width / 2
    return node.width


def _draw_edges(node: _DiagramNode, vertical_gap: float, top: float) -> str:
    lines = []
    parent_y = top + node.depth * vertical_gap + 5
    for child in node.children:
        child_y = top + child.depth * vertical_gap - 13
        lines.append(
            f'<line class="edge" x1="{node.x:.1f}" y1="{parent_y:.1f}" '
            f'x2="{child.x:.1f}" y2="{child_y:.1f}" />'
        )
        lines.append(_draw_edges(child, vertical_gap, top))
    return "".join(lines)


def _draw_nodes(node: _DiagramNode, vertical_gap: float, top: float) -> str:
    y = top + node.depth * vertical_gap
    label = escape(node.label)
    if node.kind == 'rule':
        try:
            rule_name = label.split(".")[0]
            priority_num = "." + label.split(".")[1]
            node_svg = (
                f'<g class="{node.kind}">'
                f'<title>{label}</title>'
                f"""<text x="{node.x:.1f}" y="{y:.1f}" text-anchor="middle">
                <tspan id="rulename">{rule_name}</tspan><tspan id="priority">{priority_num}</tspan></text>"""
                "</g>"
            )
        except:
            node_svg = (
                f'<g class="{node.kind}">'
                f'<title>{label}</title>'
                f"""<text x="{node.x:.1f}" y="{y:.1f}" text-anchor="middle">
                <tspan id="rulename">{label}</tspan></text>"""
                "</g>"
            )
    else:
        node_svg = (
            f'<g class="{node.kind}">'
            f'<title>{label}</title>'
            f'<text x="{node.x:.1f}" y="{y:.1f}" text-anchor="middle">{label}</text>'
            "</g>"
        )
    return node_svg + "".join(
        _draw_nodes(child, vertical_gap, top) for child in node.children
    )


def _tree_depth(node: _DiagramNode) -> int:
    return max((_tree_depth(child) for child in node.children), default=node.depth)


def render_parse_tree(tree: Tree, title: str = "Parse tree", rule_priorities=dict()) -> str:
    """Return a self-contained HTML document with a linguistic-style SVG tree."""
    safe_title = escape(title)
    root = _build_diagram_node(tree, rule_priorities)
    margin = 32
    top = 34
    vertical_gap = 58
    _measure_and_place(root)
    width = max(180, root.width + margin * 2)
    height = top + _tree_depth(root) * vertical_gap + 28
    edges = _draw_edges(root, vertical_gap, top)
    nodes = _draw_nodes(root, vertical_gap, top)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{safe_title}</title>
  <style>
    body {{ color: #202124; font: 15px/1.5 system-ui, sans-serif; margin: 1.5rem; }}
    h1 {{ font-size: 1.4rem; }}
    .diagram {{ border: 1px solid #dadce0; border-radius: 8px; overflow: auto; padding: 1rem; }}
    svg {{ display: block; font: 16px/1.2 system-ui, sans-serif; }}
    .edge {{ stroke: #202124; stroke-width: 1.2; }}
    .rule #rulename {{ fill: #0000ff; }}
    .rule #priority {{ fill: #ff0000; }}
    .terminal text {{ fill: #008000; }}
  </style>
</head>
<body>
  <h1>{safe_title}</h1>
  <div class="diagram">
    <svg xmlns="http://www.w3.org/2000/svg" width="{width:.0f}" height="{height:.0f}"
         viewBox="0 0 {width:.0f} {height:.0f}" role="img" aria-label="Parse tree">
      <g transform="translate({margin}, 0)">{edges}{nodes}</g>
    </svg>
  </div>
</body>
</html>
"""


def parse_file(
    grammar_path: str | Path,
    input_path: str | Path,
    output_path: str | Path | None = None,
    parser: str = "earley",
) -> Path:
    """Parse input_path with grammar_path and save the visual tree as HTML."""
    grammar_file = Path(grammar_path)
    source_file = Path(input_path)
    destination = (
        Path(output_path)
        if output_path is not None
        else source_file.with_name(f"{source_file.stem}.parse-tree.html")
    )

    showAllRules = False
    if showAllRules:
        with open(grammar_path, 'r') as f:
            grammar_content = f.read()
            grammar_content = re.sub(
                r"(?m)^(\s*)\?([a-z_]\w*)(?=\s*(?:\.\d+)?\s*:)",
                r"\1\2",
                grammar_content
            )
            with open('Explicit', 'w') as fw:
                fw.write(grammar_content)
                fw.close()
    
        grammar_file = Path('Explicit')

    lark = Lark.open(str(grammar_file), parser=parser, start="root",  
                     #ambiguity="explicit",
                     #lexer="dynamic",
                     )
    source = source_file.read_text(encoding="utf-8")


    tree = lark.parse(source)

    priorities = {
        rule.origin.name: rule.options.priority
        for rule in lark.rules
    }  

    try:
        print(type(tree))
        print(tree.is_ambiguous)

        # Convert the forest into a regular tree.
        trees = TreeForestTransformer().transform(tree)
        print(trees.pretty())
    except:
        pass

    destination.write_text(
        render_parse_tree(tree, f"Parse tree: {source_file.name}", rule_priorities=priorities),
        encoding="utf-8",
    )
    return destination


def main() -> int:
    cli = argparse.ArgumentParser(
        description="Parse a file with a Lark grammar and generate a visual HTML parse tree."
    )
    cli.add_argument("grammar", type=Path, help="Path to the Lark grammar file")
    cli.add_argument("input", type=Path, help="Path to the file to parse")
    cli.add_argument(
        "-o",
        "--output",
        type=Path,
        help="HTML output path (default: <input-name>.parse-tree.html)",
    )
    cli.add_argument(
        "--parser",
        choices=("earley", "lalr"),
        default="earley",
        help="Lark parser algorithm (default: earley)",
    )
    args = cli.parse_args()

    try:
        output = parse_file(args.grammar, args.input, args.output, args.parser)
    except (OSError, UnicodeError, LarkError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Parse tree written to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""
use this command: 
    python3 ParseTree.py Grammar Main
"""