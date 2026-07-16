////////////////////////////////////////////////////////////
// CRT BEZEL GAP FILLER
// Inner region flat at t_flat, outer region follows curve
// Transition based on distance from INNER cutout edge
////////////////////////////////////////////////////////////

// ---------- BEZEL INNER OPENING (mm) ----------
bezel_inner_w = 147;
bezel_inner_h = 197;

// IMPORTANT HISTORICAL PARAMETER WARNING:
// This file generates the installed bezel, but some axis names are reversed.
// The gap_long_* values are evaluated with tx(x), so they control curvature
// across the 147 mm X/width axis. The gap_short_* values are evaluated with
// ty(y), so they control curvature across the 197 mm Y/height axis.
// In other words, "long" and "short" do not match the physical long and short
// dimensions. Width/height terminology elsewhere may also feel counterintuitive.
// Do not rename, swap, or "correct" these variables without comparing the
// rendered result to the known-good final STL. Expect trial and error when
// adapting this generator to another display or enclosure.

// ---------- GAP MEASUREMENTS (lip -> LCD plane) ----------
gap_short_center  = 7.0;
gap_short_quarter = 5.0;
gap_short_corner  = 0.0;

gap_long_center  = 4.25;
gap_long_quarter = 3.25;
gap_long_corner  = 0.0;   // set 0.0 if corners touch

// ---------- STRUCTURE ----------
min_thickness = 0.8;       // do not go below this anywhere

outer_hold = 4.0;   // mm of guaranteed full-curve at the outer edge

// ---------- INNER FLAT TARGET ----------
t_flat = 1.0;              // your request: inner part equals 1 mm everywhere

// Blend control (distance measured from INNER cutout edge, outward)
// For the first flat_inner_band mm from the cutout edge, stay flat.
// Then blend up to the curved thickness over blend_band mm.
flat_inner_band = 0;

blend_band = 12;

// ---------- VIEW CUTOUT / PER-SIDE BORDERS (mm) ----------
border_left   = 16;
border_right  = 16;
border_top    = 16;
border_bottom = 16;

// Optional cutout offset if LCD is not centered
cutout_offset_x = 0;
cutout_offset_y = 0;

// Rounded inside corners of view hole
view_corner_r = 3;         // 0 = square

// ---------- RESOLUTION ----------
nx = 60;
ny = 46;


// ========================================================
// MATH
// ========================================================

function quad_coeff(c,q,k) = [
    2*(k + c - 2*q),
    (4*q - 3*c - k),
    c
];

// distance from point to nearest OUTER edge of bezel rectangle
function dist_to_outer_edge(x,y) =
    min( (bezel_inner_w/2 - abs(x)), (bezel_inner_h/2 - abs(y)) );


function quad_eval(C,t) = C[0]*t*t + C[1]*t + C[2];

function clamp01(x) = x < 0 ? 0 : (x > 1 ? 1 : x);

function smoothstep(e0, e1, x) =
    let(t = clamp01((x - e0)/(e1 - e0)))
    t*t*(3 - 2*t);

// Axis curves
longC  = quad_coeff(gap_long_center,  gap_long_quarter,  gap_long_corner);
shortC = quad_coeff(gap_short_center, gap_short_quarter, gap_short_corner);

function tx(x) = clamp01(abs(x)/(bezel_inner_w/2));
function ty(y) = clamp01(abs(y)/(bezel_inner_h/2));

function gap_xy(x,y) =
    max( quad_eval(longC,tx(x)), quad_eval(shortC,ty(y)) );

// ========================================================
// INNER CUTOUT SIZE
// ========================================================

vw = bezel_inner_w - (border_left + border_right);
vh = bezel_inner_h - (border_top + border_bottom);

vw_safe = vw < 1 ? 1 : vw;
vh_safe = vh < 1 ? 1 : vh;

// Distance from a point to the INNER cutout rectangle edge (outside the cutout).
// Uses Chebyshev style distance for blending: max(dx,dy).
function dist_to_inner_edge(x,y) =
    let(
        xi = x - cutout_offset_x,
        yi = y - cutout_offset_y,
        dx = abs(xi) - (vw_safe/2),
        dy = abs(yi) - (vh_safe/2)
    )
    max(0, max(dx, dy));

// Thickness field:
// flat near inner edge, rises toward outer edge.
// Curved target is t_flat + gap_xy.
function thickness_xy(x,y) =
    let(
        tf = max(min_thickness, t_flat),
        tc = max(min_thickness, t_flat + gap_xy(x,y)),

        d_in  = dist_to_inner_edge(x,y),
        d_out = dist_to_outer_edge(x,y),

        // 0 => flat, 1 => curved, based on distance from inner cutout edge outward
        a = smoothstep(flat_inner_band, flat_inner_band + blend_band, d_in)
    )
    // Outer band override: always curved for outer_hold mm
    (d_out <= outer_hold) ? tc : ((1 - a)*tf + a*tc);


// ========================================================
// HEIGHTFIELD SOLID
// ========================================================

module heightfield_block(w,h,nx,ny)
{
    x0 = -w/2; x1 = w/2;
    y0 = -h/2; y1 = h/2;
    dx = (x1-x0)/(nx-1);
    dy = (y1-y0)/(ny-1);

    function idx(i,j) = j*nx + i;
    top_offset = nx*ny;

    points =
        concat(
            // bottom grid
            [ for(j=[0:ny-1], i=[0:nx-1])
                [ x0 + i*dx, y0 + j*dy, 0 ] ],

            // top grid
            [ for(j=[0:ny-1], i=[0:nx-1])
                let(
                    x = x0 + i*dx,
                    y = y0 + j*dy,
                    t = thickness_xy(x,y)
                )
                [ x, y, t ]
            ]
        );

    bottom_faces =
        [ for(j=[0:ny-2], i=[0:nx-2])
            each [
                [ idx(i,j), idx(i+1,j), idx(i+1,j+1) ],
                [ idx(i,j), idx(i+1,j+1), idx(i,j+1) ]
            ]
        ];

    top_faces =
        [ for(j=[0:ny-2], i=[0:nx-2])
            let(
                a=idx(i,j)+top_offset,
                b=idx(i+1,j)+top_offset,
                c=idx(i+1,j+1)+top_offset,
                d=idx(i,j+1)+top_offset
            )
            each [
                [ a,c,b ],
                [ a,d,c ]
            ]
        ];

    side_faces =
        concat(
            [ for(i=[0:nx-2])
                let(b0=idx(i,0), b1=idx(i+1,0), t0=b0+top_offset, t1=b1+top_offset)
                each [[ b0,t1,b1 ], [ b0,t0,t1 ]]
            ],
            [ for(i=[0:nx-2])
                let(b0=idx(i,ny-1), b1=idx(i+1,ny-1), t0=b0+top_offset, t1=b1+top_offset)
                each [[ b0,b1,t1 ], [ b0,t1,t0 ]]
            ],
            [ for(j=[0:ny-2])
                let(b0=idx(0,j), b1=idx(0,j+1), t0=b0+top_offset, t1=b1+top_offset)
                each [[ b0,b1,t1 ], [ b0,t1,t0 ]]
            ],
            [ for(j=[0:ny-2])
                let(b0=idx(nx-1,j), b1=idx(nx-1,j+1), t0=b0+top_offset, t1=b1+top_offset)
                each [[ b0,t1,b1 ], [ b0,t0,t1 ]]
            ]
        );

    polyhedron(points=points, faces=concat(bottom_faces,top_faces,side_faces));
}


// ========================================================
// CUTOUT
// ========================================================

module rounded_rect_cutout(w,h,r,cut_h=300)
{
    if(r<=0)
        cube([w,h,cut_h],center=true);
    else
        linear_extrude(height=cut_h,center=true)
            offset(r=r)
                square([w-2*r,h-2*r],center=true);
}


// ========================================================
// FINAL MODEL
// ========================================================

difference()
{
    heightfield_block(bezel_inner_w,bezel_inner_h,nx,ny);

    translate([cutout_offset_x, cutout_offset_y, -1])
        rounded_rect_cutout(vw_safe, vh_safe, view_corner_r, 400);
}
