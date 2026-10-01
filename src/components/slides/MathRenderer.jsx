import React from 'react';
import katex from 'katex';

/**
 * Helper to render inline content:
 * - Parses $...$ with KaTeX inlineMode
 * - Parses **bold** into <strong className="text-white font-bold">
 */
export function renderInlineMathAndBold(text, keyPrefix = 'in') {
  if (!text) return null;

  // Support <br> or <br/> tags inside cells/text
  if (text.includes('<br') || text.includes('<BR')) {
    const parts = text.split(/<br\s*\/?>/gi);
    return parts.map((part, pIdx) => (
      <React.Fragment key={`${keyPrefix}-br-${pIdx}`}>
        {pIdx > 0 && <br />}
        {renderInlineMathAndBold(part, `${keyPrefix}-p-${pIdx}`)}
      </React.Fragment>
    ));
  }

  // Pattern matches $...$, **bold**, or *italic*
  const regex = /(\$[^$]+?\$|\*\*([^*]+?)\*\*|\*([^*]+?)\*)/g;
  const elements = [];
  let lastIndex = 0;
  let match;

  while ((match = regex.exec(text)) !== null) {
    if (match.index > lastIndex) {
      elements.push(text.substring(lastIndex, match.index));
    }

    const raw = match[0];
    if (raw.startsWith('$') && raw.endsWith('$')) {
      const math = raw.slice(1, -1).trim();
      try {
        const html = katex.renderToString(math, {
          throwOnError: false,
          displayMode: false,
        });
        elements.push(
          <span
            key={`${keyPrefix}-math-${match.index}`}
            className="inline-block mx-0.5 text-amber-200"
            dangerouslySetInnerHTML={{ __html: html }}
          />
        );
      } catch (e) {
        elements.push(<span key={`${keyPrefix}-err-${match.index}`}>{raw}</span>);
      }
    } else if (raw.startsWith('**') && raw.endsWith('**')) {
      const boldText = raw.slice(2, -2);
      elements.push(
        <strong key={`${keyPrefix}-b-${match.index}`} className="font-extrabold text-amber-300">
          {renderInlineMathAndBold(boldText, `${keyPrefix}-b`)}
        </strong>
      );
    } else if (raw.startsWith('*') && raw.endsWith('*')) {
      const italicText = raw.slice(1, -1);
      elements.push(
        <em key={`${keyPrefix}-i-${match.index}`} className="italic text-slate-300">
          {renderInlineMathAndBold(italicText, `${keyPrefix}-i`)}
        </em>
      );
    }

    lastIndex = regex.lastIndex;
  }

  if (lastIndex < text.length) {
    elements.push(text.substring(lastIndex));
  }

  return elements;
}

export default function MathRenderer({ content, className = '', inline = false }) {
  if (!content) return null;

  // If inline is requested, parse directly
  if (inline) {
    return <span className={className}>{renderInlineMathAndBold(content, 'inline')}</span>;
  }

  // Check if content contains multi-line $$...$$ blocks
  // Split content into blocks: Display Math Blocks vs Markdown Text Blocks
  const displayMathRegex = /\$\$([\s\S]*?)\$\$/g;
  const blocks = [];
  let lastIdx = 0;
  let m;

  while ((m = displayMathRegex.exec(content)) !== null) {
    if (m.index > lastIdx) {
      blocks.push({ type: 'text', value: content.substring(lastIdx, m.index) });
    }
    blocks.push({ type: 'math', value: m[1].trim() });
    lastIdx = displayMathRegex.lastIndex;
  }
  if (lastIdx < content.length) {
    blocks.push({ type: 'text', value: content.substring(lastIdx) });
  }

  return (
    <div className={`space-y-3 ${className}`}>
      {blocks.map((block, bIdx) => {
        if (block.type === 'math') {
          try {
            const html = katex.renderToString(block.value, {
              throwOnError: false,
              displayMode: true,
            });
            return (
              <div
                key={`b-math-${bIdx}`}
                className="my-3 py-3 px-4 bg-slate-950/70 border border-blue-500/20 rounded-xl overflow-x-auto text-center shadow-inner"
                dangerouslySetInnerHTML={{ __html: html }}
              />
            );
          } catch (e) {
            return (
              <pre key={`b-err-${bIdx}`} className="text-rose-400 font-mono text-xs overflow-x-auto p-2 bg-black/40 rounded">
                {block.value}
              </pre>
            );
          }
        }

        // Process Text Block: Check for Tables, Bullet Lists, and Paragraphs
        const rawLines = block.value.split('\n');
        const renderedItems = [];
        let i = 0;

        while (i < rawLines.length) {
          const line = rawLines[i].trim();

          const isDelimiterRow = (str) => {
            if (!str) return false;
            const t = str.trim();
            if (!t.startsWith('|') || !t.endsWith('|')) return false;
            const inner = t.slice(1, -1);
            const cols = inner.split('|');
            return cols.length >= 1 && cols.every(col => /^[\s\-:]+$/.test(col) && col.includes('-'));
          };

          // Check if it's the start of a Markdown Table (starts and ends with |)
          if (line.startsWith('|') && line.endsWith('|') && i + 1 < rawLines.length && isDelimiterRow(rawLines[i + 1])) {
            const tableLines = [];
            while (i < rawLines.length && rawLines[i].trim().startsWith('|') && rawLines[i].trim().endsWith('|')) {
              tableLines.push(rawLines[i].trim());
              i++;
            }

            if (tableLines.length >= 2) {
              const parseRow = (rowStr) =>
                rowStr
                  .split('|')
                  .slice(1, -1)
                  .map((cell) => cell.trim());

              const headerCells = parseRow(tableLines[0]);
              // skip tableLines[1] because it's delimiter
              const dataRows = tableLines.slice(2).map(parseRow);

              renderedItems.push(
                <div key={`tbl-${bIdx}-${i}`} className="my-4 overflow-x-auto rounded-2xl border-2 border-blue-500/40 bg-slate-950/90 shadow-2xl backdrop-blur-md">
                  <table className="w-full text-left border-collapse">
                    <thead className="bg-gradient-to-r from-blue-900/90 via-slate-900/90 to-indigo-950/90 border-b-2 border-blue-500/40 text-xs md:text-sm font-black uppercase tracking-wider text-amber-300">
                      <tr>
                        {headerCells.map((h, hIdx) => (
                          <th key={hIdx} className="py-2.5 px-4 border-r border-slate-700/60 last:border-none shadow-sm">
                            {renderInlineMathAndBold(h, `th-${hIdx}`)}
                          </th>
                        ))}
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-800 text-xs md:text-sm lg:text-base">
                      {dataRows.map((row, rIdx) => (
                        <tr key={rIdx} className="hover:bg-blue-500/10 transition-colors duration-150 odd:bg-slate-900/40 even:bg-slate-950/70">
                          {row.map((cell, cIdx) => (
                            <td key={cIdx} className="py-2.5 px-4 text-slate-100 border-r border-slate-800/70 last:border-none leading-relaxed">
                              {renderInlineMathAndBold(cell, `td-${rIdx}-${cIdx}`)}
                            </td>
                          ))}
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              );
              continue;
            }
          }

          // Bullet List Items: starts with - or *
          if (line.startsWith('- ') || line.startsWith('* ')) {
            const bulletText = line.substring(2).trim();
            renderedItems.push(
              <div key={`li-${bIdx}-${i}`} className="flex items-start gap-2.5 my-1.5 text-xs md:text-sm text-slate-200">
                <span className="w-2 h-2 rounded-full bg-amber-400 mt-1.5 shrink-0 shadow-sm shadow-amber-400/50" />
                <div className="flex-1 leading-relaxed">
                  {renderInlineMathAndBold(bulletText, `li-${i}`)}
                </div>
              </div>
            );
            i++;
            continue;
          }

          // Regular Non-Empty Paragraph
          if (line.length > 0) {
            renderedItems.push(
              <div key={`p-${bIdx}-${i}`} className="text-xs md:text-sm text-slate-200 leading-relaxed my-1">
                {renderInlineMathAndBold(line, `p-${i}`)}
              </div>
            );
          }

          i++;
        }

        return <React.Fragment key={`blk-${bIdx}`}>{renderedItems}</React.Fragment>;
      })}
    </div>
  );
}
