from flask import Flask, request, render_template_string, jsonify
import re

app = Flask(__name__)

# Mapping from https://github.com/ilovecats4606/fx-82AU-PLUS-II-2nd/blob/main/tokentable.md (used chatgpt to help convert to dict hopefully this is right)
TOKEN_MAP = {
    0x00: 'null',
    0x01: 'mᴘ',
    0x02: 'mn',
    0x03: 'me',
    0x04: 'm𝜇',
    0x05: 'ao',
    0x06: 'h',
    0x07: '𝜇ɴ',
    0x08: '𝜇ʙ',
    0x09: 'ħ',
    0x0A: 'α',
    0x0B: 're',
    0x0C: '𝜆c',
    0x0D: 'γᴘ',
    0x0E: 'γcp',
    0x0F: '𝜆cn',
    0x10: 'Σx²',
    0x11: 'Σx',
    0x12: 'n',
    0x13: 'Σy²',
    0x14: 'Σy',
    0x15: 'Σxy',
    0x16: 'Σy³',
    0x17: '∑x²y',
    0x18: '∑x⁴',
    0x19: 'minX',
    0x1A: 'maxX',
    0x1B: 'minY',
    0x1C: 'maxY',
    0x1D: 'R∞',
    0x1E: 'u',
    0x1F: '𝜇ᴘ',
    0x20: 'AtWt ',
    0x21: '▯',
    0x22: '𝜇e',
    0x23: '𝜇n',
    0x24: '𝜇𝜇',
    0x25: '%',
    0x26: 'F',
    0x27: 'e',
    0x28: '(',
    0x29: ')',
    0x2A: 'Nᴀ',
    0x2B: '+',
    0x2C: ',',
    0x2D: '-',
    0x2E: '.',
    0x2F: '.+1',
    0x30: '0',
    0x31: '1',
    0x32: '2',
    0x33: '3',
    0x34: '4',
    0x35: '5',
    0x36: '6',
    0x37: '7',
    0x38: '8',
    0x39: '9',
    0x3A: ':',
    0x3B: 'k',
    0x3C: '<',
    0x3D: '=',
    0x3E: '>',
    0x3F: 'RndFix(',
    0x40: 'Vm',
    0x41: 'A',
    0x42: 'B',
    0x43: 'C',
    0x44: 'D',
    0x45: 'E',
    0x46: 'F',
    0x47: '->A',
    0x48: '->B',
    0x49: '->C',
    0x4A: '->D',
    0x4B: '->E',
    0x4C: '->F',
    0x4D: '->Y',
    0x4E: '×',
    0x4F: '÷',
    0x50: 'h',
    0x51: 'c',
    0x52: 'o',
    0x53: 'b',
    0x54: 'M',
    0x55: '▶a+b𝐢',
    0x56: '▶r∠𝜃',
    0x57: '!',
    0x58: 'X',
    0x59: 'Y',
    0x5A: 'Ref(',
    0x5B: 'Rref(',
    0x5C: '▫',
    0x5D: 'π(',
    0x5E: '^( ',
    0x5F: '÷R',
    0x60: '(-)',
    0x61: 'Not(',
    0x62: 'Neg(',
    0x63: 'Abs(',
    0x64: 'x̂₁',
    0x65: 'x̂',
    0x66: 'ŷ',
    0x67: 'x̂₂',
    0x68: 'log(',
    0x69: 'Σ(',
    0x6A: '∫(',
    0x6B: 'd/dx(',
    0x6C: 'Pol(',
    0x6D: 'Rec(',
    0x6E: 'and',
    0x6F: 'or',
    0x70: 'sinh(',
    0x71: 'cosh(',
    0x72: 'tanh(',
    0x73: '𝒆^(',
    0x74: 'x10',
    0x75: '^2',
    0x76: '^3',
    0x77: '^-1',
    0x78: 'R',
    0x79: 'c₀',
    0x7A: 'c₁',
    0x7B: 'Int(',
    0x7C: '@',
    0x7D: 'Intg(',
    0x7E: 'xor',
    0x7F: 'xnor',
    0x80: '𝐢',
    0x81: '𝒆',
    0x82: 'π',
    0x83: '->E',
    0x84: '->F',
    0x85: '°',
    0x86: 'ʳ',
    0x87: 'ᵍ',
    0x88: 'Conjg(',
    0x89: 'x̄',
    0x8A: 'ȳ',
    0x8B: 'Ans',
    0x8C: 'Ran#',
    0x8D: 'Q1',
    0x8E: 'Q3',
    0x8F: 'med',
    0x90: 'sinh⁻¹(',
    0x91: 'cosh⁻¹(',
    0x92: 'tanh⁻¹(',
    0x93: '10^(',
    0x94: '≤',
    0x95: '≠',
    0x96: '≥',
    0x97: '▶Simp ',
    0x98: '√(',
    0x99: 'M+',
    0x9A: 'ᴀ',
    0x9B: 'ʙ',
    0x9C: 'ᴄ',
    0x9D: 'r',
    0x9E: '⋅',
    0x9F: 'ˣ√(',
    0xA0: 'sin(',
    0xA1: 'cos(',
    0xA2: 'tan(',
    0xA3: 'ln(',
    0xA4: '(',
    0xA5: '▶Conv ',
    0xA6: 'GCD(',
    0xA7: 'LCM(',
    0xA8: '³√(',
    0xA9: 'M-',
    0xAA: '𝜎x',
    0xAB: 'sx',
    0xAC: '𝜎y',
    0xAD: 'sy',
    0xAE: '⌟',
    0xAF: '∠',
    0xB0: 'sin⁻¹(',
    0xB1: 'cos⁻¹(',
    0xB2: 'tan⁻¹(',
    0xB3: 'Rnd(',
    0xB4: 'c₂',
    0xB5: '𝜎',
    0xB6: '𝜀₀',
    0xB7: '𝜇₀',
    0xB8: '𝗔',
    0xB9: '𝗕',
    0xBA: '𝗖',
    0xBB: '𝗗',
    0xBC: '𝗘',
    0xBD: '𝗙',
    0xBE: '𝗣',
    0xBF: '𝗖',
    0xC0: 'det(',
    0xC1: 'Trn(',
    0xC2: 'RanInt#(',
    0xC3: 'arg(',
    0xC4: '𝜙₀',
    0xC5: 'g',
    0xC6: 'G₀',
    0xC7: 'Z₀',
    0xC8: 'MatA',
    0xC9: 'MatB',
    0xCA: 'MatC',
    0xCB: 'MatAns',
    0xCC: 'VctA',
    0xCD: 'VctB',
    0xCE: 'VctC',
    0xCF: 'VctAns',
    0xD0: 'P(',
    0xD1: 'Q(',
    0xD2: 'R(',
    0xD3: '▶t',
    0xD4: 't',
    0xD5: 'G',
    0xD6: 'atm',
    0xD7: 'in▶cm',
    0xD8: 'cm▶in',
    0xD9: 'ft▶m',
    0xDA: 'm▶ft',
    0xDB: 'yd▶m',
    0xDC: 'm▶yd',
    0xDD: 'mile▶km',
    0xDE: 'km▶mile',
    0xDF: 'n mile▶m',
    0xE0: 'm▶n mile',
    0xE1: 'acre▶m²',
    0xE2: 'm²▶acre',
    0xE3: 'gal(US)▶ℓ',
    0xE4: 'ℓ▶gal(US)',
    0xE5: 'gal(UK)▶ℓ',
    0xE6: 'ℓ▶gal(UK)',
    0xE7: 'pc▶km',
    0xE8: 'km▶pc',
    0xE9: 'km/h▶m/s',
    0xEA: 'm/s▶km/h',
    0xEB: 'oz▶g',
    0xEC: 'g▶oz',
    0xED: 'lb▶kg',
    0xEE: 'kg▶lb',
    0xEF: 'atm▶Pa',
    0xF0: 'Pa▶atm',
    0xF1: 'mmHg▶Pa',
    0xF2: 'Pa▶mmHg',
    0xF3: 'hp▶kW',
    0xF4: 'kW▶hp',
    0xF5: 'kgf/cm²▶Pa',
    0xF6: 'Pa▶kgf/cm²',
    0xF7: 'kgf⋅m▶J',
    0xF8: 'J▶kgf⋅m',
    0xF9: 'lbf/in²▶kPa',
    0xFA: 'kPa▶lbf/in²',
    0xFB: '°F▶°C',
    0xFC: '°C▶°F',
    0xFD: 'J▶cal',
    0xFE: 'cal▶J',
    0xFF: '@',
}


# Require unstable in lineio verify
_unstable_ranges = [
    (0x00, 0x24),
    (0x26, 0x2A),
    (0x2F, 0x2F),
    (0x3A, 0x3E),
    (0x40, 0x40),
    (0x47, 0x4D),
    (0x50, 0x53),
    (0x55, 0x56),
    (0x5A, 0x5B),
    (0x5D, 0x5F),
    (0x61, 0x67),
    (0x69, 0x6F),
    (0x77, 0x80),
    (0x83, 0x8A),
    (0x8D, 0x8E),
    (0x8F, 0x8F),
    (0x93, 0x97),
    (0x99, 0x9E),
    (0xA4, 0xA7),
    (0xA9, 0xAF),
    (0xB4, 0xC1),
    (0xC3, 0xFF),
]
UNSTABLE_SET = set()
for a, b in _unstable_ranges:
    for v in range(a, b + 1):
        UNSTABLE_SET.add(v)

# find the last typeable token from the whole table
LAST_TYPEABLE_TOKEN = None
for val, token in sorted(TOKEN_MAP.items()):
    if val not in UNSTABLE_SET and token != '<UNK>':
        LAST_TYPEABLE_TOKEN = token


# display <UNK> for unknown tokens

HEX_SPLIT_RE = re.compile(r"[\s,;]+")
HEX_ITEM_RE = re.compile(r"^(?:0x)?([0-9a-fA-F]{1,2})(?:h|H)?$")

# pretty html cause why not
HTML = r"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>fx-82AU Plus II 2nd Token Translator</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">
  <style>
    :root{--bg:#0f1724;--card:#0b1220;--accent:#7c3aed;--muted:#94a3b8;--glass:rgba(255,255,255,0.03)}
    *{box-sizing:border-box;font-family:Inter,system-ui,Segoe UI,Roboto,'Helvetica Neue',Arial}
    body{margin:0;background:linear-gradient(135deg,#071029 0%, #07132a 60%);color:#e6eef8;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:48px}
    .card{width:880px;max-width:96%;background:var(--card);border-radius:16px;padding:22px;box-shadow:0 8px 30px rgba(2,6,23,0.6);backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,0.03);}
    h1{margin:0 0 6px;font-weight:800;letter-spacing:-0.6px}
    p.lead{margin:0;color:var(--muted);font-size:14px}
    .grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:18px}
    textarea,input{width:100%;padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,0.04);background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));color:inherit;resize:vertical}
    .controls{display:flex;gap:8px;margin-top:12px}
    button{background:linear-gradient(90deg,var(--accent),#4f46e5);border:0;padding:10px 14px;border-radius:10px;color:white;font-weight:600;cursor:pointer;box-shadow:0 6px 18px rgba(124,58,237,0.18);transition:transform .18s ease,box-shadow .18s}
    button.secondary{background:transparent;border:1px solid rgba(255,255,255,0.06);color:var(--muted);box-shadow:none}
    button:active{transform:translateY(1px)}
    .result{background:var(--glass);padding:12px;border-radius:10px;min-height:120px;overflow:auto;border:1px solid rgba(255,255,255,0.02)}
    .row{display:flex;gap:10px;align-items:center}
    .chip{background:rgba(255,255,255,0.03);padding:6px 10px;border-radius:999px;font-weight:600;display:inline-block}
    .tokens{margin-top:10px;white-space:pre-wrap;font-family:monospace}
    .small{font-size:13px;color:var(--muted)}
    .anim-fade{opacity:0;transform:translateY(6px);animation:fadeIn .5s forwards}
    @keyframes fadeIn{to{opacity:1;transform:none}}
    .footer{display:flex;justify-content:space-between;align-items:center;margin-top:14px}
    .copy{background:transparent;border:0;color:var(--muted);cursor:pointer}
    .table-preview{margin-top:12px;max-height:220px;overflow:auto;border-radius:8px;padding:8px;background:rgba(255,255,255,0.02)}
    table{width:100%;border-collapse:collapse;font-size:13px}
    td,th{padding:6px 8px;border-bottom:1px solid rgba(255,255,255,0.02)}
    th{color:var(--muted);text-align:left;font-weight:600}
    /* unstable styling */
    .unstable {
      color: #ff9a2e;
      font-weight: 700;
      cursor: help;
      position: relative;
      text-decoration: underline dotted;
      display: inline-block;
    }
    .unstable:hover::after {
      content: attr(title);
      position: absolute;
      bottom: 100%;
      left: 50%;
      transform: translateX(-50%);
      padding: 5px;
      background: rgba(0,0,0,0.8);
      color: white;
      border-radius: 4px;
      font-size: 12px;
      white-space: nowrap;
      z-index: 100;
    }
    .totals{margin-bottom:8px;font-family:Inter,system-ui,Segoe UI,Roboto,'Helvetica Neue',Arial}
  </style>
</head>
<body>
  <div class="card anim-fade">
    <h1>fx-82AU Plus II 2nd Token Translator</h1>
    <p class="lead">Paste hex bytes (space/comma separated). Accepts <code>F9</code>, <code>0xF9</code>, or <code>F9h</code>.</p>

    <div class="grid">
      <div>
        <label class="small">Input hex bytes</label>
        <textarea id="hexin" rows="6" placeholder="e.g. F9 F7 F7H or 30 31 32"></textarea>

        <div class="controls">
          <button id="translate">TRANSLATE TO HACKSTRING TOKENS</button>
          <button id="preview" class="secondary">Preview tokens table</button>
          <button id="clear" class="secondary">Clear</button>
        </div>

        <div class="small" style="margin-top:8px">You can paste bytes separated by spaces, commas or newlines. Unknown bytes are shown as &lt;UNK&gt;.</div>
      </div>

      <div>
        <label class="small">Output</label>
        <div class="result" id="result">
          <div class="small">No translation yet - click <strong>TRANSLATE TO HACKSTRING TOKENS</strong>.</div>
        </div>

        <div class="footer">
          <div class="small">
          <a href="https://github.com/ilovecats4606/fx-82AU-PLUS-II-2nd/blob/main/tokentable.md" target="_blank">Token table by ilovecats4606 here.</a> 
          <div>
            <button id="copy" class="copy">Copy</button>
          </div>
        </div>
      </div>
    </div>

    <div id="tableContainer" class="table-preview" style="display:none">
      <table>
        <thead><tr><th>Hex</th><th>Token</th><th>Unstable</th></tr></thead>
        <tbody id="tableBody"></tbody>
      </table>
    </div>
  </div>

<script>
const tokenizeEndpoint = '/api/translate';

function escapeHtml(s){return s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('\n','<br>')}

function parseResponse(resp){
  // resp: { items: [...], totals: {...} }
  const outParts = [];
  const items = resp.items || [];
  // build totals display
  const totals = resp.totals || {};
  const totalsHtml = `<div class="totals small">
    <strong>Total:</strong> ${totals.total || 0} &nbsp;&middot;&nbsp;
    <strong>Typeable:</strong> ${totals.typeable_count || 0} &nbsp;&middot;&nbsp;
    <strong>Unstable needed:</strong> ${totals.unstable_count || 0} &nbsp;&middot;&nbsp;
    <strong>Unknown:</strong> ${totals.unknown_count || 0}
  </div>`;

  for(const item of items){
    const hex = item.hex.padEnd(4,' ');
    // if unstable, wrap token in span with class unstable and title from server
    if(item.unstable){
      const title = item.overflow_from || 'Overflow from empty';
      outParts.push(`${hex}\t<span class="unstable" title="${escapeHtml(title)}">${escapeHtml(item.token)}</span>`);
    } else {
      // normal token (or <UNK>)
      outParts.push(`${hex}\t${escapeHtml(item.token)}`);
    }
  }
  return totalsHtml + '<div class="tokens">' + outParts.join('<br>') + '</div>';
}

async function translate(){
  const val = document.getElementById('hexin').value.trim();
  const resDiv = document.getElementById('result');
  if(!val){resDiv.innerHTML = '<div class="small">Please enter some hex bytes.</div>';return}
  resDiv.innerHTML = '<div class="small">Translating…</div>';
  try{
    const r = await fetch(tokenizeEndpoint,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({text:val})});
    const j = await r.json();
    const pretty = parseResponse(j);
    resDiv.innerHTML = pretty;
  }catch(e){
    resDiv.innerHTML = '<div class="small">Error translating — see console.</div>';
    console.error(e);
  }
}

function buildTable(){
  const container = document.getElementById('tableBody');
  fetch('/api/table').then(r=>r.json()).then(j=>{
    container.innerHTML = '';
    for(const row of j.rows){
      const tr = document.createElement('tr');
      const td1 = document.createElement('td'); td1.textContent = row.hex;
      const td2 = document.createElement('td'); 
      td2.textContent = row.token;
      if(row.unstable){
        td2.classList.add('unstable');
        td2.title = 'Unstable - requires overflow (cannot be typed directly)';
      }
      const td3 = document.createElement('td');
      td3.textContent = row.unstable ? 'Yes' : '';
      if(row.unstable) td3.classList.add('small');
      tr.appendChild(td1);tr.appendChild(td2);tr.appendChild(td3);container.appendChild(tr);
    }
  });
}

document.getElementById('translate').addEventListener('click',translate);

document.getElementById('preview').addEventListener('click',()=>{
  const tc = document.getElementById('tableContainer');
  if(tc.style.display==='none'){ buildTable(); tc.style.display='block'; } else { tc.style.display='none'}
});

document.getElementById('clear').addEventListener('click',()=>{document.getElementById('hexin').value='';document.getElementById('result').innerHTML='<div class="small">Cleared.</div>'})

document.getElementById('copy').addEventListener('click',()=>{
  const t = document.querySelector('.result .tokens');
  if(!t) return;
  navigator.clipboard.writeText(t.innerText).then(()=>{alert('Copied to clipboard')});
});
</script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/api/translate', methods=['POST'])
def api_translate():
    data = request.get_json() or {}
    text = data.get('text','')
    parts = HEX_SPLIT_RE.split(text.strip())
    items = []

    total = 0
    typeable_count = 0
    unstable_count = 0
    unknown_count = 0

    for p in parts:
        if not p: continue
        total += 1
        m = HEX_ITEM_RE.match(p.strip())
        val = None
        if not m:
            # try to salvage by removing trailing non-hex
            clean = re.sub(r'[^0-9a-fA-F]','',p)
            if len(clean)==0:
                items.append({'hex':'??','token':'<UNK>','unstable': False, 'overflow_from': None})
                unknown_count += 1
                continue
            if len(clean)==1: clean = '0'+clean
            try:
                val = int(clean,16)
            except:
                items.append({'hex':'??','token':'<UNK>','unstable': False, 'overflow_from': None})
                unknown_count += 1
                continue
        else:
            val = int(m.group(1),16)
        tok = TOKEN_MAP.get(val, '<UNK>')
        unstable = val in UNSTABLE_SET
        overflow_from = None
        if unstable:
          unstable_count += 1
          # for bytes 00–24 and other early unstable ranges
          if _unstable_ranges[0][0] <= val <= _unstable_ranges[0][1]:
              overflow_from = "Overflow from empty"
          else:
              overflow_from = f"Overflow from {LAST_TYPEABLE_TOKEN}"
        else:
            if tok != '<UNK>':
                typeable_count += 1
            else:
                unknown_count += 1
        items.append({'hex': format(val,'02X'), 'token': tok, 'unstable': unstable, 'overflow_from': overflow_from})
    totals = {
        'total': total,
        'typeable_count': typeable_count,
        'unstable_count': unstable_count,
        'unknown_count': unknown_count
    }
    return jsonify({'items': items, 'totals': totals})

@app.route('/api/table')
def api_table():
    rows = []
    for k in sorted(TOKEN_MAP.keys()):
        rows.append({'hex': format(k,'02X'), 'token': TOKEN_MAP[k], 'unstable': (k in UNSTABLE_SET)})
    return jsonify({'rows': rows})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
