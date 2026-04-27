import json, math

with open('C:/Users/yerid/AppData/Local/Temp/ne110.json', encoding='utf-8') as f:
    data = json.load(f)

WANT = {'United States of America': 'us', 'Mexico': 'mx', 'Belize': 'bz'}
features = {}
for feat in data['features']:
    name = feat['properties'].get('NAME') or feat['properties'].get('name') or feat['properties'].get('SOVEREIGNT')
    if name in WANT:
        features[WANT[name]] = feat

# Bounding box (combined region of interest, EXCLUDING Alaska/Hawaii — focus on contiguous US south through Belize)
LON_MIN, LON_MAX = -125.0, -86.5
LAT_MIN, LAT_MAX = 14.0, 50.0

# Equirectangular with cosine correction at mean latitude (gives proportional shapes near our region)
MEAN_LAT_RAD = math.radians((LAT_MIN + LAT_MAX) / 2)
COS_LAT = math.cos(MEAN_LAT_RAD)

# Choose px/lat-degree so things are reasonably sized
PX_PER_LAT = 25.0
PX_PER_LON = PX_PER_LAT * COS_LAT

W = (LON_MAX - LON_MIN) * PX_PER_LON
H = (LAT_MAX - LAT_MIN) * PX_PER_LAT

print(f"viewBox: 0 0 {W:.2f} {H:.2f}")
print(f"COS_LAT={COS_LAT:.4f}, PX_PER_LAT={PX_PER_LAT}, PX_PER_LON={PX_PER_LON:.4f}")

def proj(lon, lat):
    x = (lon - LON_MIN) * PX_PER_LON
    y = (LAT_MAX - lat) * PX_PER_LAT
    return x, y

def ring_to_path(ring):
    pts = []
    for i, (lon, lat) in enumerate(ring):
        # Skip points outside or wildly far from the region for US (clip Alaska, Hawaii)
        x, y = proj(lon, lat)
        cmd = 'M' if i == 0 else 'L'
        pts.append(f"{cmd}{x:.2f} {y:.2f}")
    pts.append('Z')
    return ''.join(pts)

def feature_to_path(feat, clip_to_view=False):
    geom = feat['geometry']
    rings = []
    if geom['type'] == 'Polygon':
        rings = geom['coordinates']
    elif geom['type'] == 'MultiPolygon':
        for poly in geom['coordinates']:
            rings.extend(poly)
    parts = []
    for ring in rings:
        if clip_to_view:
            in_view = any(LON_MIN - 5 < lon < LON_MAX + 5 and LAT_MIN - 5 < lat < LAT_MAX + 5 for lon, lat in ring)
            if not in_view:
                continue
        parts.append(ring_to_path(ring))
    return ' '.join(parts)

paths = {}
for code, feat in features.items():
    paths[code] = feature_to_path(feat, clip_to_view=(code == 'us'))

# Cities (lon, lat)
cities = [
    ('TUCSON', -110.926, 32.222),
    ('CIDADE DO MÉXICO', -99.133, 19.432),
    ('PUNTA GORDA', -88.806, 16.099),
]

# Build SVG
svg_lines = []
svg_lines.append(f'<?xml version="1.0" encoding="UTF-8" standalone="no"?>')
svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.2f} {H:.2f}" preserveAspectRatio="xMidYMid meet">')
svg_lines.append(f'  <title>Mapa: Estados Unidos, México e Belize</title>')
svg_lines.append(f'  <desc>Mapa estilizado mostrando os tres paises da biografia linguistica, com marcadores em Tucson, Cidade do Mexico e Punta Gorda.</desc>')
svg_lines.append(f'  <g fill="none" stroke="#e8b56a" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round">')
for code in ('us', 'mx', 'bz'):
    svg_lines.append(f'    <path id="{code}" d="{paths[code]}"/>')
svg_lines.append(f'  </g>')

# City markers
svg_lines.append(f'  <g fill="#e8b56a" stroke="#0a0e1a" stroke-width="1.5">')
for name, lon, lat in cities:
    x, y = proj(lon, lat)
    svg_lines.append(f'    <circle cx="{x:.2f}" cy="{y:.2f}" r="6.5"/>')
svg_lines.append(f'  </g>')

# City labels
svg_lines.append(f'  <g fill="#f5f1e8" font-family="Space Grotesk, sans-serif" font-size="20" font-weight="600" letter-spacing="2">')
# Tucson: label up-right
x, y = proj(-110.926, 32.222)
svg_lines.append(f'    <text x="{x+12:.2f}" y="{y-10:.2f}">TUCSON</text>')
# Cidade do Mexico: label down-left to avoid going off frame
x, y = proj(-99.133, 19.432)
svg_lines.append(f'    <text x="{x-145:.2f}" y="{y+5:.2f}">CIDADE DO MÉXICO</text>')
# Punta Gorda: label to the LEFT of the dot so it does not overflow the right edge of the viewBox
x, y = proj(-88.806, 16.099)
svg_lines.append(f'    <text x="{x-12:.2f}" y="{y+5:.2f}" text-anchor="end">PUNTA GORDA</text>')
svg_lines.append(f'  </g>')

svg_lines.append('</svg>')

out = 'C:/Users/yerid/Documents/HBHP/10sem/POR305/biografia/BiografiaMarioMorales/assets/MapNorthAmerica.svg'
with open(out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(svg_lines))
print(f"\nWrote {out}")
print(f"Cities at:")
for n, lon, lat in cities:
    x, y = proj(lon, lat)
    print(f"  {n}: ({x:.1f}, {y:.1f})")
