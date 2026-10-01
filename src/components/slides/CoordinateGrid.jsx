import React from 'react';

/**
 * CoordinateGrid: Interactive/Visual Cartesian Coordinate Plane (Cartesian Coordinate System)
 * Renders an exact, high-clarity 2D Cartesian grid for developmental algebra students.
 * Supports:
 * - Grid lines with numerical tick marks (-10 to 10 by default)
 * - X and Y axes with bold directional arrows and labels
 * - Plotted points with glowing rings, pulsating markers, and coordinate callouts
 * - Plotted linear equations (standard, slope-intercept, vertical x=c, horizontal y=c)
 * - Rise/Run slope triangles with delta-y and delta-x labels
 * - Shaded domain/range intervals or function curves
 */
export default function CoordinateGrid({
  width = 460,
  height = 420,
  xMin = -8,
  xMax = 8,
  yMin = -8,
  yMax = 8,
  xTicks: propXTicks = null,
  yTicks: propYTicks = null,
  points = [],
  lines = [],
  curves = [],
  slopeTriangle = null,
  title = "Cartesian Coordinate Plane (x, y)",
  vltLine = null, // x value for vertical line test demonstration
  axisOfSymmetry = null // x value for parabola axis of symmetry
}) {
  const padding = 35;
  const plotWidth = width - padding * 2;
  const plotHeight = height - padding * 2;

  // Coordinate transforms
  const toSvgX = (x) => padding + ((x - xMin) / (xMax - xMin)) * plotWidth;
  const toSvgY = (y) => padding + ((yMax - y) / (yMax - yMin)) * plotHeight;

  // Smart step calculation
  const getStep = (min, max, stepProp) => {
    if (typeof stepProp === 'number' && stepProp > 0) return stepProp;
    const span = Math.abs(max - min);
    if (span <= 14) return 1;
    if (span <= 28) return 2;
    if (span <= 60) return 5;
    if (span <= 120) return 10;
    return Math.ceil(span / 10);
  };

  const xStep = getStep(xMin, xMax, propXTicks);
  const yStep = getStep(yMin, yMax, propYTicks);

  const xTicks = [];
  if (Array.isArray(propXTicks)) {
    xTicks.push(...propXTicks);
  } else {
    const start = Math.ceil(xMin / xStep) * xStep;
    for (let x = start; x <= xMax; x += xStep) {
      if (x !== 0) xTicks.push(x);
    }
  }

  const yTicks = [];
  if (Array.isArray(propYTicks)) {
    yTicks.push(...propYTicks);
  } else {
    const start = Math.ceil(yMin / yStep) * yStep;
    for (let y = start; y <= yMax; y += yStep) {
      if (y !== 0) yTicks.push(y);
    }
  }

  const originX = toSvgX(0);
  const originY = toSvgY(0);

  // Pre-calculate placed bounding boxes to avoid overlap
  const placedBoxes = [];

  // If axisOfSymmetry exists, reserve its label area
  if (axisOfSymmetry !== null) {
    placedBoxes.push({
      x: toSvgX(axisOfSymmetry) + 6,
      y: padding + 6,
      width: 130,
      height: 18
    });
  }

  // Helper to check if two rects intersect (with 4px safety buffer)
  const isIntersecting = (r1, r2, margin = 4) => {
    return !(
      r1.x + r1.width + margin <= r2.x ||
      r2.x + r2.width + margin <= r1.x ||
      r1.y + r1.height + margin <= r2.y ||
      r2.y + r2.height + margin <= r1.y
    );
  };

  // Determine parabola direction if curves are present (default opens up)
  const mainCurve = curves.find((c) => c.a !== undefined);
  const opensUp = mainCurve ? mainCurve.a > 0 : true;

  // Process points with collision avoidance
  const computedPoints = points.map((pt) => {
    const rawLabel = pt.label || `(${pt.x}, ${pt.y})`;
    const cx = toSvgX(pt.x);
    const cy = toSvgY(pt.y);
    const boxWidth = Math.max(rawLabel.length * 6.8 + 12, 36);
    const boxHeight = 18;

    // If explicit offsets are specified, respect them directly
    if (pt.labelOffsetX !== undefined || pt.labelOffsetY !== undefined) {
      const x = cx + (pt.labelOffsetX !== undefined ? pt.labelOffsetX : 8);
      const y = cy + (pt.labelOffsetY !== undefined ? pt.labelOffsetY : -20);
      const box = { x, y, width: boxWidth, height: boxHeight };
      placedBoxes.push(box);
      return { ...pt, label: rawLabel, cx, cy, boxWidth, boxHeight, boxX: x, boxY: y };
    }

    const isVertex = /v|vertex|min|max/i.test(rawLabel);
    const isYIntercept = Math.abs(pt.x) < 0.001 || /y-int/i.test(rawLabel);
    const isXIntercept = Math.abs(pt.y) < 0.001 || /x-int/i.test(rawLabel);

    // Build prioritized candidate positions
    const candidates = [];

    if (isVertex) {
      if (opensUp) {
        // Vertex is at the bottom (minimum) -> place label BELOW the vertex
        candidates.push({ x: cx - boxWidth / 2, y: cy + 12 });
        candidates.push({ x: cx + 10, y: cy + 10 });
        candidates.push({ x: cx - boxWidth - 10, y: cy + 10 });
        candidates.push({ x: cx - boxWidth / 2, y: cy - boxHeight - 12 });
      } else {
        // Vertex is at the top (maximum) -> place label ABOVE the vertex
        candidates.push({ x: cx - boxWidth / 2, y: cy - boxHeight - 12 });
        candidates.push({ x: cx + 10, y: cy - boxHeight - 8 });
        candidates.push({ x: cx - boxWidth - 10, y: cy - boxHeight - 8 });
        candidates.push({ x: cx - boxWidth / 2, y: cy + 12 });
      }
    } else if (isYIntercept) {
      // For y-intercept, usually on vertical axis: prefer side with more space
      candidates.push({ x: cx + 12, y: cy - boxHeight / 2 });
      candidates.push({ x: cx - boxWidth - 12, y: cy - boxHeight / 2 });
      candidates.push({ x: cx + 12, y: cy - boxHeight - 6 });
      candidates.push({ x: cx - boxWidth - 12, y: cy - boxHeight - 6 });
    } else if (isXIntercept) {
      // Check relative position to axis of symmetry or midpoint
      const center = axisOfSymmetry !== null ? axisOfSymmetry : 0;
      if (pt.x < center) {
        // Left root: offset top-left so it stays away from vertex
        candidates.push({ x: cx - boxWidth - 8, y: cy - boxHeight - 6 });
        candidates.push({ x: cx - boxWidth - 8, y: cy + 10 });
        candidates.push({ x: cx - boxWidth / 2, y: cy - boxHeight - 12 });
        candidates.push({ x: cx + 8, y: cy - boxHeight - 6 });
      } else {
        // Right root: offset top-right so it stays away from vertex
        candidates.push({ x: cx + 8, y: cy - boxHeight - 6 });
        candidates.push({ x: cx + 8, y: cy + 10 });
        candidates.push({ x: cx - boxWidth / 2, y: cy - boxHeight - 12 });
        candidates.push({ x: cx - boxWidth - 8, y: cy - boxHeight - 6 });
      }
    } else {
      // General point
      candidates.push({ x: cx + 10, y: cy - boxHeight - 6 });
      candidates.push({ x: cx - boxWidth - 10, y: cy - boxHeight - 6 });
      candidates.push({ x: cx + 10, y: cy + 8 });
      candidates.push({ x: cx - boxWidth - 10, y: cy + 8 });
      candidates.push({ x: cx - boxWidth / 2, y: cy - boxHeight - 12 });
      candidates.push({ x: cx - boxWidth / 2, y: cy + 12 });
    }

    // Clamp candidate within SVG bounds
    const clampCandidate = (cand) => {
      let x = Math.max(padding + 2, Math.min(width - padding - boxWidth - 2, cand.x));
      let y = Math.max(padding + 2, Math.min(height - padding - boxHeight - 2, cand.y));
      return { x, y, width: boxWidth, height: boxHeight };
    };

    // Find best candidate with zero (or minimum) overlaps
    let chosenBox = clampCandidate(candidates[0]);
    let minOverlaps = 999;

    for (const cand of candidates) {
      const box = clampCandidate(cand);
      let overlaps = 0;
      for (const placed of placedBoxes) {
        if (isIntersecting(box, placed)) {
          overlaps++;
        }
      }
      if (overlaps === 0) {
        chosenBox = box;
        minOverlaps = 0;
        break;
      }
      if (overlaps < minOverlaps) {
        minOverlaps = overlaps;
        chosenBox = box;
      }
    }

    // Secondary fallback: if still overlapping, nudge vertically
    if (minOverlaps > 0) {
      for (const offset of [22, -22, 40, -40]) {
        const shifted = clampCandidate({ x: chosenBox.x, y: chosenBox.y + offset });
        if (!placedBoxes.some((p) => isIntersecting(shifted, p))) {
          chosenBox = shifted;
          break;
        }
      }
    }

    placedBoxes.push(chosenBox);

    return {
      ...pt,
      label: rawLabel,
      cx,
      cy,
      boxWidth,
      boxHeight,
      boxX: chosenBox.x,
      boxY: chosenBox.y
    };
  });

  return (
    <div className="flex flex-col items-center bg-slate-950/90 rounded-2xl p-4 border border-blue-500/30 shadow-2xl backdrop-blur-md max-w-full">
      {title && (
        <div className="flex items-center justify-between w-full px-2 mb-2 text-xs font-bold text-slate-300 border-b border-slate-800 pb-1.5 gap-3">
          <span className="flex items-center gap-1.5 text-blue-400 truncate flex-1 min-w-0" title={title}>
            <span className="w-2 h-2 rounded-full bg-blue-500 animate-pulse shrink-0"></span>
            <span className="truncate">{title}</span>
          </span>
          <span className="text-[10px] text-slate-400 font-mono shrink-0 whitespace-nowrap bg-slate-900/80 px-2 py-0.5 rounded border border-slate-800">
            x: [{xMin}, {xMax}], y: [{yMin}, {yMax}]
          </span>
        </div>
      )}

      <svg
        viewBox={`0 0 ${width} ${height}`}
        className="w-full h-auto max-h-[380px] select-none"
        style={{ filter: "drop-shadow(0 4px 12px rgba(0,0,0,0.5))" }}
      >
        <defs>
          {/* Arrow markers */}
          <marker id="axis-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#94a3b8" />
          </marker>
          <marker id="axis-arrow-blue" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#38bdf8" />
          </marker>
          {/* Glowing dot filter */}
          <filter id="glow-gold" x="-50%" y="-50%" width="200%" height="200%">
            <feDropShadow dx="0" dy="0" stdDeviation="3" floodColor="#f59e0b" floodOpacity="0.8" />
          </filter>
          <filter id="glow-blue" x="-50%" y="-50%" width="200%" height="200%">
            <feDropShadow dx="0" dy="0" stdDeviation="3" floodColor="#38bdf8" floodOpacity="0.8" />
          </filter>
          <filter id="glow-emerald" x="-50%" y="-50%" width="200%" height="200%">
            <feDropShadow dx="0" dy="0" stdDeviation="3" floodColor="#10b981" floodOpacity="0.8" />
          </filter>
          <clipPath id="grid-plot-area">
            <rect x={padding} y={padding} width={plotWidth} height={plotHeight} />
          </clipPath>
        </defs>

        {/* Background Grid Lines */}
        <g stroke="#1e293b" strokeWidth="1" strokeDasharray="2,2">
          {xTicks.map((x) => (
            <line key={`grid-x-${x}`} x1={toSvgX(x)} y1={padding} x2={toSvgX(x)} y2={height - padding} />
          ))}
          {yTicks.map((y) => (
            <line key={`grid-y-${y}`} x1={padding} y1={toSvgY(y)} x2={width - padding} y2={toSvgY(y)} />
          ))}
        </g>

        {/* Primary Axes */}
        {/* X-Axis */}
        <line
          x1={padding - 10}
          y1={originY}
          x2={width - padding + 10}
          y2={originY}
          stroke="#94a3b8"
          strokeWidth="2.5"
          markerEnd="url(#axis-arrow)"
          markerStart="url(#axis-arrow)"
        />
        {/* Y-Axis */}
        <line
          x1={originX}
          y1={height - padding + 10}
          x2={originX}
          y2={padding - 10}
          stroke="#94a3b8"
          strokeWidth="2.5"
          markerEnd="url(#axis-arrow)"
          markerStart="url(#axis-arrow)"
        />

        {/* Axis Labels */}
        <text x={width - padding + 18} y={originY + 4} fill="#38bdf8" fontSize="13" fontWeight="bold" fontFamily="sans-serif">
          x
        </text>
        <text x={originX - 4} y={padding - 16} fill="#38bdf8" fontSize="13" fontWeight="bold" fontFamily="sans-serif">
          y
        </text>

        {/* Origin Label */}
        <text x={originX - 14} y={originY + 16} fill="#64748b" fontSize="10" fontFamily="sans-serif">
          (0,0)
        </text>

        {/* X-Axis Ticks & Numbers */}
        {xTicks.map((x) => (
          <g key={`tick-x-${x}`}>
            <line x1={toSvgX(x)} y1={originY - 3} x2={toSvgX(x)} y2={originY + 3} stroke="#64748b" strokeWidth="1.5" />
            {(xTicks.length <= 16 || x % 2 === 0) && (
              <text
                x={toSvgX(x)}
                y={originY + 14}
                fill="#94a3b8"
                fontSize="9"
                fontWeight="500"
                textAnchor="middle"
                fontFamily="sans-serif"
              >
                {x}
              </text>
            )}
          </g>
        ))}

        {/* Y-Axis Ticks & Numbers */}
        {yTicks.map((y) => (
          <g key={`tick-y-${y}`}>
            <line x1={originX - 3} y1={toSvgY(y)} x2={originX + 3} y2={toSvgY(y)} stroke="#64748b" strokeWidth="1.5" />
            {(yTicks.length <= 16 || y % 2 === 0) && (
              <text
                x={originX - 8}
                y={toSvgY(y) + 3}
                fill="#94a3b8"
                fontSize="9"
                fontWeight="500"
                textAnchor="end"
                fontFamily="sans-serif"
              >
                {y}
              </text>
            )}
          </g>
        ))}

        {/* Lines */}
        {lines.map((ln, idx) => {
          const color = ln.color || (idx === 0 ? "#38bdf8" : "#ec4899");
          let x1, y1, x2, y2;

          if (ln.vertical !== undefined) {
            // Vertical line x = c
            x1 = ln.vertical;
            y1 = yMin;
            x2 = ln.vertical;
            y2 = yMax;
          } else if (ln.horizontal !== undefined) {
            // Horizontal line y = c
            x1 = xMin;
            y1 = ln.horizontal;
            x2 = xMax;
            y2 = ln.horizontal;
          } else if (ln.slope !== undefined && ln.yIntercept !== undefined) {
            // y = mx + b
            x1 = xMin;
            y1 = ln.slope * x1 + ln.yIntercept;
            x2 = xMax;
            y2 = ln.slope * x2 + ln.yIntercept;
          } else if (ln.p1 && ln.p2) {
            // Through two points
            const m = (ln.p2[1] - ln.p1[1]) / (ln.p2[0] - ln.p1[0]);
            const b = ln.p1[1] - m * ln.p1[0];
            x1 = xMin;
            y1 = m * x1 + b;
            x2 = xMax;
            y2 = m * x2 + b;
          }

          return (
            <g key={`line-${idx}`}>
              <line
                x1={toSvgX(x1)}
                y1={toSvgY(y1)}
                x2={toSvgX(x2)}
                y2={toSvgY(y2)}
                stroke={color}
                strokeWidth={ln.strokeWidth || 3}
                strokeDasharray={ln.dashed ? "6,4" : undefined}
                style={{ filter: "drop-shadow(0 2px 6px rgba(0,0,0,0.6))" }}
              />
              {ln.label && (
                <rect
                  x={toSvgX(ln.labelX || (x1 + x2) / 2) - 30}
                  y={toSvgY(ln.labelY || (y1 + y2) / 2) - 18}
                  width="70"
                  height="18"
                  rx="4"
                  fill="#090d16"
                  stroke={color}
                  strokeWidth="1"
                />
              )}
              {ln.label && (
                <text
                  x={toSvgX(ln.labelX || (x1 + x2) / 2) + 5}
                  y={toSvgY(ln.labelY || (y1 + y2) / 2) - 5}
                  fill={color}
                  fontSize="10"
                  fontWeight="bold"
                  textAnchor="middle"
                  fontFamily="sans-serif"
                >
                  {ln.label}
                </text>
              )}
            </g>
          );
        })}

        {/* Curves (Parabolas y = ax^2 + bx + c or Functions) */}
        <g clipPath="url(#grid-plot-area)">
          {curves.map((c, cIdx) => {
            const color = c.color || "#38bdf8";
            const samples = 140;
            const pointsList = [];
            for (let i = 0; i <= samples; i++) {
              const x = xMin + (i / samples) * (xMax - xMin);
              let y;
              if (c.a !== undefined) {
                y = c.a * x * x + (c.b || 0) * x + (c.c || 0);
              } else if (typeof c.fn === 'function') {
                y = c.fn(x);
              } else {
                y = 0;
              }
              pointsList.push(`${toSvgX(x)},${toSvgY(y)}`);
            }
            const d = `M ${pointsList.join(" L ")}`;
            return (
              <g key={`curve-${cIdx}`}>
                <path
                  d={d}
                  fill="none"
                  stroke={color}
                  strokeWidth={c.strokeWidth || 3}
                  strokeDasharray={c.dashed ? "6,4" : undefined}
                  style={{ filter: "drop-shadow(0 2px 6px rgba(0,0,0,0.6))" }}
                />
              </g>
            );
          })}
        </g>

        {/* Axis of Symmetry (for Parabolas) */}
        {axisOfSymmetry !== null && (
          <g>
            <line
              x1={toSvgX(axisOfSymmetry)}
              y1={padding}
              x2={toSvgX(axisOfSymmetry)}
              y2={height - padding}
              stroke="#f59e0b"
              strokeWidth="2"
              strokeDasharray="5,4"
            />
            <rect
              x={toSvgX(axisOfSymmetry) + 6}
              y={padding + 6}
              width="130"
              height="18"
              rx="4"
              fill="#090d16"
              stroke="#f59e0b"
              strokeWidth="1"
            />
            <text
              x={toSvgX(axisOfSymmetry) + 71}
              y={padding + 19}
              fill="#fbbf24"
              fontSize="9"
              fontWeight="bold"
              textAnchor="middle"
              fontFamily="sans-serif"
            >
              Axis of Symmetry (x = {axisOfSymmetry})
            </text>
          </g>
        )}

        {/* Slope Triangle (Rise / Run) */}
        {slopeTriangle && (
          <g>
            {/* Run: Horizontal dashed line */}
            <line
              x1={toSvgX(slopeTriangle.x1)}
              y1={toSvgY(slopeTriangle.y1)}
              x2={toSvgX(slopeTriangle.x2)}
              y2={toSvgY(slopeTriangle.y1)}
              stroke="#f59e0b"
              strokeWidth="2"
              strokeDasharray="4,3"
            />
            {/* Rise: Vertical dashed line */}
            <line
              x1={toSvgX(slopeTriangle.x2)}
              y1={toSvgY(slopeTriangle.y1)}
              x2={toSvgX(slopeTriangle.x2)}
              y2={toSvgY(slopeTriangle.y2)}
              stroke="#10b981"
              strokeWidth="2"
              strokeDasharray="4,3"
            />
            {/* Run Label */}
            <text
              x={(toSvgX(slopeTriangle.x1) + toSvgX(slopeTriangle.x2)) / 2}
              y={toSvgY(slopeTriangle.y1) + 14}
              fill="#fbbf24"
              fontSize="10"
              fontWeight="bold"
              textAnchor="middle"
              fontFamily="sans-serif"
            >
              Run = {slopeTriangle.run}
            </text>
            {/* Rise Label */}
            <text
              x={toSvgX(slopeTriangle.x2) + 8}
              y={(toSvgY(slopeTriangle.y1) + toSvgY(slopeTriangle.y2)) / 2 + 4}
              fill="#34d399"
              fontSize="10"
              fontWeight="bold"
              fontFamily="sans-serif"
            >
              Rise = {slopeTriangle.rise}
            </text>
          </g>
        )}

        {/* Vertical Line Test (VLT) demonstration */}
        {vltLine !== null && (
          <g>
            <line
              x1={toSvgX(vltLine)}
              y1={padding}
              x2={toSvgX(vltLine)}
              y2={height - padding}
              stroke="#ef4444"
              strokeWidth="2.5"
              strokeDasharray="5,3"
            />
            <text
              x={toSvgX(vltLine) + 6}
              y={padding + 16}
              fill="#f87171"
              fontSize="10"
              fontWeight="bold"
              fontFamily="sans-serif"
            >
              VLT Line (x={vltLine})
            </text>
          </g>
        )}

        {/* Plotted Points with Anti-Collision Label Boxes */}
        {computedPoints.map((pt, idx) => {
          const color = pt.color || "#f59e0b";
          const filterId = pt.color === "#38bdf8" ? "glow-blue" : pt.color === "#10b981" ? "glow-emerald" : "glow-gold";

          return (
            <g key={`point-${idx}`}>
              {/* Pulsing outer ring */}
              <circle cx={pt.cx} cy={pt.cy} r="9" fill={color} fillOpacity="0.2" stroke={color} strokeWidth="1" />
              {/* Solid point */}
              <circle cx={pt.cx} cy={pt.cy} r="5" fill={color} filter={`url(#${filterId})`} />
              {/* Label box */}
              <rect
                x={pt.boxX}
                y={pt.boxY}
                width={pt.boxWidth}
                height={pt.boxHeight}
                rx="4"
                fill="#090d16"
                stroke={color}
                strokeWidth="1.2"
                opacity="0.95"
              />
              {/* Label text */}
              <text
                x={pt.boxX + pt.boxWidth / 2}
                y={pt.boxY + 13}
                fill="#f8fafc"
                fontSize="10"
                fontWeight="bold"
                textAnchor="middle"
                fontFamily="sans-serif"
              >
                {pt.label}
              </text>
            </g>
          );
        })}
      </svg>
    </div>
  );
}
